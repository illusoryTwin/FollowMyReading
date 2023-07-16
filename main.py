import os
import shutil
from typing import List

from fastapi_users import FastAPIUsers

from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.responses import FileResponse
from starlette.background import BackgroundTasks

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from modules.archive_modules.zip_archiver import zip_add_file
from modules.audio_modules.AudioFileWithText import AudioFileWithText
from modules.image_modules.ImageWithText import ImageWithText
from modules.image_modules.ImageToSentences import ImageWithText as ImageWithTextSentences


app = FastAPI(
    title="Follow My Reading App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.post("/image_to_strings")
def image_process(background_tasks: BackgroundTasks, user: User = Depends(current_user), file: UploadFile = File(...)):
    contents = file.file.read()
    with open("modules/image_modules/images/" + file.filename, 'wb') as f:
        f.write(contents)
    image_file = ImageWithTextSentences("modules/image_modules/images/" + file.filename)
    background_tasks.add_task(os.remove, "modules/image_modules/images/" + file.filename)
    return image_file.get_sentences()


# First file - audio, second file - image
@app.post("/audio_split_by_image")
def audio_split_by_image(background_tasks: BackgroundTasks,  user: User = Depends(current_user),
                         files: List[UploadFile] = File(...)):
    image_file = files[1]
    image_contents = image_file.file.read()
    with open("modules/image_modules/images/" + image_file.filename, 'wb') as f:
        f.write(image_contents)
    image_obj = ImageWithText("modules/image_modules/images/" + image_file.filename)
    last_words_from_image = image_obj.get_last_word_of_every_sentence()
    audio_file = files[0]
    audio_contents = audio_file.file.read()
    with open("modules/audio_modules/audios/" + audio_file.filename, 'wb') as f:
        f.write(audio_contents)
    audio_file_obj = AudioFileWithText("modules/audio_modules/audios/" + audio_file.filename)
    audio_segments = audio_file_obj.split_audio_by_last_words(last_words_from_image)
    zip_file_name = "modules/audio_modules/audios/" + audio_file.filename[:-4] + "/" + audio_file.filename + ".zip"
    os.mkdir("modules/audio_modules/audios/" + audio_file.filename[:-4])
    for num_of_seg, segment in enumerate(audio_segments):
        output_file = "modules/audio_modules/audios/" + audio_file.filename[:-4] + f"/audio_chunk_{num_of_seg}.mp3"
        segment.export(output_file, format="mp3")
        zip_add_file(zip_file_name, output_file)
    background_tasks.add_task(shutil.rmtree, "modules/audio_modules/audios/" + audio_file.filename[:-4])
    background_tasks.add_task(os.remove, "modules/audio_modules/audios/" + audio_file.filename)
    background_tasks.add_task(os.remove, "modules/image_modules/images/" + image_file.filename)
    return FileResponse(path=zip_file_name, filename=audio_file.filename[:-4] + ".zip", background=background_tasks)


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym."

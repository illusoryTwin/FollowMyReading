import os
import shutil
from typing import List, Tuple

from fastapi_users import FastAPIUsers

from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.responses import FileResponse
from starlette.background import BackgroundTasks

from app.auth.auth import auth_backend
from app.auth.database import User
from app.auth.manager import get_user_manager
from app.auth.schemas import UserRead, UserCreate
from app.modules.archive_modules.zip_archiver import zip_add_file
from app.modules.audio_modules.AudioToTranscription import AudioFileWithText as AudioFileWithTextTranscription
from app.modules.audio_modules.AudioFileWithText import AudioFileWithText
from app.modules.image_modules.ImageWithText import ImageWithText
from app.modules.image_modules.ImageToSentences import ImageWithText as ImageWithTextSentences
from app.modules.text_module.LastWordsFromText import LastSentencesWords
from app.schemas.main_schema import sentences_list, file_with_body, orig_strings_and_transcription

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

upload_image_path = "app/modules/image_modules/uploaded_images/"
upload_audio_path = "app/modules/audio_modules/uploaded_audios/"
complete_audio_path = "app/modules/audio_modules/complete_audios/"


@app.post("/image_to_strings")
def image_to_string(background_tasks: BackgroundTasks, user: User = Depends(current_user),
                    file: UploadFile = File(...)):
    contents = file.file.read()
    with open(upload_image_path + file.filename, 'wb') as f:
        f.write(contents)
    image_file = ImageWithTextSentences(upload_image_path + file.filename)
    background_tasks.add_task(os.remove, upload_image_path + file.filename)
    return image_file.get_sentences()


@app.post("/audio_split_by_strings")
def audio_split_by_strings(background_tasks: BackgroundTasks, include_transcription: orig_strings_and_transcription,
                           user: User = Depends(current_user), string_with_sentences: sentences_list = Depends(),
                           file: UploadFile = File(...)):
    contents = file.file.read()
    with open(upload_audio_path + file.filename, 'wb') as f:
        f.write(contents)
    last_words = LastSentencesWords(string_with_sentences.sentences).get_last_word_of_every_sentence()
    audio_file = AudioFileWithText(upload_audio_path + file.filename)
    audio_segments = audio_file.split_audio_by_last_words(last_words)
    zip_file_name = complete_audio_path + file.filename[:-4] + "/" + file.filename + ".zip"
    os.mkdir(complete_audio_path + file.filename[:-4])
    for num_of_seg, segment in enumerate(audio_segments):
        output_zip_file = complete_audio_path + file.filename[:-4] + f"/audio_chunk_{num_of_seg}.mp3"
        segment.export(output_zip_file, format="mp3")
        zip_add_file(zip_file_name, output_zip_file)
    background_tasks.add_task(shutil.rmtree, complete_audio_path + file.filename[:-4])
    background_tasks.add_task(os.remove, upload_audio_path + file.filename)
    if include_transcription.value == "yes":
        audio_transcription_file = AudioFileWithTextTranscription(upload_audio_path + file.filename)
        audio_transcription = audio_transcription_file.get_timed_recognised_text()
        return file_with_body(file=FileResponse(path=zip_file_name, filename=file.filename[:-4] + ".zip"),
                              original_strings=string_with_sentences.sentences, audio_transcription=audio_transcription)
    return FileResponse(path=zip_file_name, filename=file.filename[:-4] + ".zip")


# First file - audio, second file - image
@app.post("/audio_split_by_image")
def audio_split_by_image(background_tasks: BackgroundTasks,  user: User = Depends(current_user),
                         audio_file: UploadFile = File(...), image_file: UploadFile = File(...)):
    image_contents = image_file.file.read()
    with open(upload_image_path + image_file.filename, 'wb') as f:
        f.write(image_contents)
    image_obj = ImageWithText(upload_image_path + image_file.filename)
    last_words_from_image = image_obj.get_last_word_of_every_sentence()
    audio_contents = audio_file.file.read()
    with open(upload_audio_path + audio_file.filename, 'wb') as f:
        f.write(audio_contents)
    audio_file_obj = AudioFileWithText(upload_audio_path + audio_file.filename)
    audio_segments = audio_file_obj.split_audio_by_last_words(last_words_from_image)
    zip_file_name = complete_audio_path + audio_file.filename[:-4] + "/" + audio_file.filename + ".zip"
    os.mkdir(complete_audio_path + audio_file.filename[:-4])
    for num_of_seg, segment in enumerate(audio_segments):
        output_zip_file = complete_audio_path + audio_file.filename[:-4] + f"/audio_chunk_{num_of_seg}.mp3"
        segment.export(output_zip_file, format="mp3")
        zip_add_file(zip_file_name, output_zip_file)
    background_tasks.add_task(shutil.rmtree, complete_audio_path + audio_file.filename[:-4])
    background_tasks.add_task(os.remove, upload_audio_path + audio_file.filename)
    background_tasks.add_task(os.remove, upload_image_path + image_file.filename)
    return FileResponse(path=zip_file_name, filename=audio_file.filename[:-4] + ".zip", background=background_tasks)


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym."

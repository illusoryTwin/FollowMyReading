from fastapi_users import FastAPIUsers

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from modules.audio_modules.audio_word_cutter import audio_cutter

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


@app.post("/audio_splitter")
def upload(file: UploadFile = File(...)):
    contents = file.file.read()
    with open("modules/audio_modules/audios/" + file.filename, 'wb') as f:
        f.write(contents)
    print(audio_cutter("modules/audio_modules/audios/" + file.filename))

    return FileResponse(path="modules/audio_modules/audios/" + file.filename + ".zip", filename=file.filename+".zip")


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym."

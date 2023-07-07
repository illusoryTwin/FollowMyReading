import os

from fastapi_users import FastAPIUsers

from fastapi import FastAPI, UploadFile, File

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from modules.image_modules.ImageWithText import ImageWithText


app = FastAPI(
    title="Follow My Reading API"
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


@app.post("/image_to_text")
def audio_process(uploaded_file: UploadFile = File(...)):
    uploaded_file_content = uploaded_file.file.read()
    with open("modules/image_modules/images/" + uploaded_file.filename, 'wb') as f:
        f.write(uploaded_file_content)
    image = ImageWithText("modules/image_modules/images/" + uploaded_file.filename)
    last_words_array = image.get_last_word_of_every_sentence()
    os.remove("modules/image_modules/images/" + uploaded_file.filename)
    return last_words_array


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym."

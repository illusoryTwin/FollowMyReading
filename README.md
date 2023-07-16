![BADGE](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
## Name
API service "Follow My Reading"

## Description
An API service for image text extraction, audio-to-text transcription, and audio splitting by sentences in English, Russian, and Arabic languages.

## Demo
[Folder with screenshots of API service](https://drive.google.com/drive/folders/1PJPPnRNsXcRtLpPQDVCZ5eay4i48E-zz)

## How to use

To utilize our API service, you can make POST requests to the following endpoints hosted at [http://217.18.62.143:8000](http://217.18.62.143:8000):

- /auth/jwt/login: Use this endpoint to authenticate and obtain a JWT token for subsequent requests.

- /auth/jwt/logout: This endpoint allows a user to invalidate and log out of the current session by revoking the JWT token.

- /auth/register: Register a new user account using this endpoint. Provide the necessary details to create a new account securely.

- /image_to_strings: Submit a POST request to this endpoint with an image file as input. Our API will extract the text from the image and return a list of strings as a response.

- /audio_split_by_strings: Use this endpoint to transcribe an audio file to text. The API will split the audio into segments based on sentence breaks and return the corresponding text.

- /audio_split_by_strings_additional: Similar to /audio_split_by_strings, this endpoint provides additional functionality by including audio transcription and original text.

- /audio_split_by_image: Submit a POST request to this endpoint with both an audio file and an image file. The API will match the audio segments with the corresponding text on the image and returns a link to the splitted audio files.

Make sure to include the necessary parameters and data in your POST requests according to the API documentation. Link to documentation : [http://217.18.62.143:8000/docs#/](http://217.18.62.143:8000/docs#/).


## Features list

- **Audio-to-Text Transcription**: Converts audio files into textual representations. The API accepts audio files in wav and mp3 formats and returns the transcribed text.

- **Image Text Extraction**: Extracts text from images. The API accepts image file in jpeg and png formats and returns text from it.

- **Multilingual Support**: Our API supports English, Russian, and Arabic languages for both audio-to-text transcription and image text extraction.

- **Audio-Text Synchronization**: The API offers the ability to match audio segments with the corresponding text on an image.

- **Audio Splitting**: The API splits an audio file into separate audio files, each contains a single sentence.

- **JWT Authentication**: Secure your API access using JSON Web Tokens (JWT). The API includes authentication endpoints for user registration, login, and logout, ensuring the protection of user data and access control.

## Installation using Docker

To run this application using Docker, follow the steps below:

1. Clone the repository:

<div class="termy">

```bash
$ git clone <repository_url>
$ cd <repository_directory>
```

</div>

2. Build and run the Docker containers using docker-compose:

Use -d option for detached mode.

```bash
$ docker-compose up
```
The FastAPI application will be accessible at http://0.0.0.0:8000.

Note: Make sure Docker and docker-compose are installed and running on your system before executing the above commands.
3. Fill the role table
For authorization to work correctly you need to fill the role table with at least 1 role, to choose it, during registration



   
## Clean installation

To run this application on your machine without docker containers:

Clone the repository:

<div class="termy">

```bash
$ git clone <repository_url>
$ cd <repository_directory>
```

</div>

Note: you will need only app directory and requirements.

Install frameworks required for correct work.


<div class="termy">

Install a multimedia framework for handling audio processing:

```bash
$ apt-get install -y ffmpeg
```

Install the tesseract-ocr package for character recognition:
```bash
$ apt-get install -y tesseract-ocr
```

Install an additional package for Tesseract OCR specifically for Russian language support:
```bash
$ apt-get install -y tesseract-ocr tesseract-ocr-rus
```

Download a file that contains language data used by Tesseract OCR for Arabic language text recognition:
```bash
$ wget https://github.com/tesseract-ocr/tessdata/raw/main/ara.traineddata
```

Move the downloaded "ara.traineddata" file to the appropriate directory:
```bash
$ mv ara.traineddata /usr/share/tesseract-ocr/5/tessdata/
```

</div>


Secondly, install python requirements:

<div class="termy">

```bash
$ pip install --no-cache-dir --upgrade -r /app/requirements.txt
```

</div>

After that:
- create directory 'versions' in the path 'app/migrations/'
- create directories 'complete_audios' and 'uploaded_audios' in the path 'app/modules/audio_modules/'
- create directory 'uploaded_images' in the path 'app/modules/image_modules/'

## Requirements for running

To run this project, ensure that PostgreSQL is running. Set up the environmental variables for connecting to the database in the .env file.

## Migrations

To initialize migrations you need to make an alembic revision:

<div class="termy">

```bash
$ alembic revision --autogenerate -m 'name_of_revision'
```

</div>

And upgrade head after revision:

<div class="termy">

```bash
$ alembic upgrade head
```

</div>


## Run it

Run the server with:
<div class="termy">

```bash
$ uvicorn main:app --host localhost --port 8000 --log-level 'trace'
```

</div>

## Frameworks and technologies used
The following frameworks and technologies were used in this project:

- OpenAI Whisper
- PyDub
- PyTesseract
- Unittest
- PostgreSQL

## For customer
[Linux server tutorial](https://www.youtube.com/watch?v=WMy3OzvBWc0)

[Tutorial postgreSQL](https://www.youtube.com/watch?v=qw--VYLpxG4)

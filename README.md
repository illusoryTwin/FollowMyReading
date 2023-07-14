# Follow My Reading


## Installation

Firstly, install frameworks required for correct work


<div class="termy">

```console
$ apt-get install -y ffmpeg
$ apt-get install -y tesseract-ocr
```

</div>


Secondly, install python requirements

<div class="termy">

```console
$ pip install --no-cache-dir --upgrade -r /app/requirements.txt
```

</div>

After that:
- create directory 'versions' in the path 'migrations/'
- create directories 'audios'  in the path 'modules/audio_modules/'
- create directory 'images' in the path 'modules/image_modules/'

## Requirements for running

You need to have running PostgreSQL to run this project, environmental variables for connection to DataBse can be set up in .env file.

## Migrations

To initialize migrations you need to make an alembic revision:

<div class="termy">

```console
$ alembic revision --autogenerate -m 'name_of_revision'
```

</div>

And upgrade head after revision:

<div class="termy">

```console
$ alembic upgrade head
```

</div>


## Run it

Run the server with:
<div class="termy">

```console
$ uvicorn main:app --host localhost --port 8000 --log-level 'trace'
```

</div>
FROM python:3.10
RUN apt-get update
RUN apt-get install -y ffmpeg
RUN apt-get install -y git
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y tesseract-ocr tesseract-ocr-rus
WORKDIR /usr/share/tesseract-ocr/5/tessdata/
RUN wget https://github.com/tesseract-ocr/tessdata/raw/main/ara.traineddata
WORKDIR /
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app /app
WORKDIR app
WORKDIR migrations
RUN mkdir -p versions
WORKDIR ../
WORKDIR modules
WORKDIR audio_modules
RUN mkdir -p complete_audios
RUN mkdir -p uploaded_audios
WORKDIR ../
WORKDIR image_modules
WORKDIR uploaded_images
WORKDIR /
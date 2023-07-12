# IMAGE RECOGNITION FOR DIFFERENT LANGUAGES

# DEPENDENCIES
# apt install tesseract-ocr
# pip install pytesseract

# # For russian
# sudo apt-get install -y tesseract-ocr tesseract-ocr-rus

# # For arabic
# wget https://github.com/tesseract-ocr/tessdata/raw/main/ara.traineddata
# mv ara.traineddata /usr/share/tesseract-ocr/4.00/tessdata/

import re
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

class ImageWithText:
    """Class for handling an image with text."""

    def __init__(self, image: str):
        """Initializes the class with an image."""
        self.image = image

    def get_sentences(self, lang_code: str):
        """
        Extract text from the image and split it into individual sentences.
        Returns a list of strings, where each string represents a sentence from the image.
        """
        if lang_code == 'Unknown language':
            print("Unsupported language!")
            return None
        # Extract text from the image
        image_text = pytesseract.image_to_string(self.image, lang=lang_code)

        # # Split the text into sentences
        sentences = re.split('(?<=[.!?])', image_text)
        return sentences


# # Example of usage
# lang_checker = LanguageChecker('russian')
# lang_code = lang_checker.get_lang_code()
#
# image = ImageWithText(Image.open('russian.jpg'))
# text = image.get_sentences(lang_code)
# print(text)
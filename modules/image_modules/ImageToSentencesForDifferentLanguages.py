# !apt install tesseract-ocr
# !pip install pytesseract
# # # For russian
# !sudo apt-get install -y tesseract-ocr tesseract-ocr-rus
#
# # # For arabic
# !wget https://github.com/tesseract-ocr/tessdata/raw/main/ara.traineddata
# !mv ara.traineddata /usr/share/tesseract-ocr/4.00/tessdata/

import re
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


class LanguageChecker:
    """Class to check the language and return specific results."""

    def __init__(self, language: str):
        """Initialize the class with a language."""
        self.language = language.lower()

    def get_lang_code(self):
        """Return specific results based on the language."""
        if self.language == 'english':
            return 'eng'
        elif self.language == 'russian':
            return 'rus'
        elif self.language == 'arabic':
            return 'ara'
        else:
            return 'Unknown language'


class ImageWithText:
    """Class for handling an image with text."""

    def __init__(self, image: Image):
        """Initializes the class with an image."""
        self.image = image

    # def get_last_word_of_every_sentence(self, lang_code: str):
    #     """
    #     Extract text from the image and find the last word of each sentence.
    #     """
    #     if lang_code == 'Unknown language':
    #         print("Unsupported language!")
    #         return None

    #     # Extract text from the image
    #     image_text = pytesseract.image_to_string(self.image, lang=lang_code)

    #     return image_text

    def get_sentences(self, lang_code: str):
        """
        Extract text from the image and split it into individual sentences.
        Returns a list of strings, where each string represents a sentence from the image.
        """
        if lang_code == 'Unknown language':
            print("Unsupported language!")
            return None
        # Extract text from the image
        image_text = pytesseract.image_to_string(self.image, lang="rus")

        # # Split the text into sentences
        sentences = re.split('(?<=[.!?])', image_text)
        return sentences
        return sentencees


# # Example of usage
#
# lang_checker = LanguageChecker('english')
# lang_code = lang_checker.get_lang_code()
#
# image = ImageWithText(Image.open('russian.jpg'))
# last_words = image.get_sentences(lang_code)
# print(last_words)
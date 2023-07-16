import re
import pytesseract
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

class ImageWithText:
    """Class for handling an image with text."""

    def __init__(self, image: Image):
        """Initializes the class with an image."""
        self.image = image

    def get_sentences(self, lang_code: str, signs=None):
        """
        Extract text from the image and split it into individual sentences.
        Returns a list of strings, where each string represents a sentence from the image.
        """
        if lang_code == 'Unknown language':
            print("Unsupported language!")
            return None

        # Extract text from the image
        image_text = pytesseract.image_to_string(self.image, lang=lang_code)

        if signs is None:
            signs = r'[.!?]'
        else:
            # Escape special characters in the provided signs, including comma
            signs = re.escape(''.join(signs))

        pattern = f'(?<=[{signs}])'  # Include comma in the lookbehind assertion
        # Split the text into sentences
        sentences = re.split(pattern, image_text)
        return sentences


# # Example of usage
#
# lang_checker = LanguageChecker('arabic')
# lang_code = lang_checker.get_lang_code()
#
# image = ImageWithText(Image.open('arabic2.png'))
#
# # signs = [".", "?"]
# # last_words = image.get_sentences(lang_code, signs)
#
# # signs = ["ب"]
# # last_words = image.get_sentences(lang_code, signs)
#
# last_words = image.get_sentences(lang_code)
# print(last_words)

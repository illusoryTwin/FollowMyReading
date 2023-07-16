<<<<<<< Updated upstream:modules/image_modules/ImageToSentences.py
# !apt install tesseract-ocr
# !pip install pytesseract

=======
import re
>>>>>>> Stashed changes:app/modules/image_modules/ImageToSentences.py
import pytesseract
from PIL import Image

#pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


class ImageToSentences:
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

<<<<<<< Updated upstream:modules/image_modules/ImageToSentences.py
    @staticmethod
    def find_word_before_punct_mark(text):
        """
        Function to find the last word before each punctuation mark in the text.
        """
        words_array = text.split(" ")
        last_words_array = []
        sentence_end_marks = ['.', ',', '?', '!']

        for word_index in range(len(words_array)):
            if words_array[word_index] in sentence_end_marks:
                if word_index > 0:
                    word_before_dot = words_array[word_index - 1]
                    last_words_array.append(word_before_dot)

        return last_words_array

    def get_sentences(self):
        """
        Extract text from the image.
        Returns a string that represents the extracted text from the image.
        """
        # Extract text from the image
        image_text = pytesseract.image_to_string(self.image)
        return image_text

# # Example of usage
# image = Image.open("часть 1.png")
# image_with_text = ImageWithText(image)
# sentences = image_with_text.get_sentences()
# print(sentences)
=======
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
>>>>>>> Stashed changes:app/modules/image_modules/ImageToSentences.py

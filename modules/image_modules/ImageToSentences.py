# !apt install tesseract-ocr
# !pip install pytesseract

import pytesseract
from PIL import Image


class ImageWithText:
    """Class for handling an image with text."""

    def __init__(self, image: Image):
        """Initializes the class with an image."""
        self.image = image

    @staticmethod
    def insert_space_before_punct_mark(text):
        """
        Function to insert a space before each punctuation mark in the text.
        """
        sentence_end_marks = ['.', ',', '?', '!']
        for mark in sentence_end_marks:
            text = text.replace(mark, f' {mark}')
        return text

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
        Extract text from the image and find the last word of each sentence.
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
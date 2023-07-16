import pytesseract


class ImageWithText:
    """Class for handling an image with text."""

    def __init__(self, image: str):
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

    def get_last_word_of_every_sentence(self):
        """
        Extract text from the image and find the last word of each sentence.
        """
        # Extract text from the image
        image_text = pytesseract.image_to_string(self.image)

        # Format the text by inserting a space before each punctuation mark
        formatted_text = self.insert_space_before_punct_mark(image_text)

        # Find the last word of each sentence
        last_words = self.find_word_before_punct_mark(formatted_text)

        return last_words

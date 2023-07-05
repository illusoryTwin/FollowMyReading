import pytesseract
from PIL import Image


def insert_space_before_dot(text):
    # Function to insert a space before each dot in the text
    text_with_space = text.replace('.', ' .')
    return text_with_space


def find_word_before_dot(text):
    # Function to find the word before each dot in the text
    words_array = text.split(" ")
    last_words = []
    sentence_end_mark = ['.', ',', '?', '!']

    for word_index in range(len(words_array)):
        if words_array[word_index] in sentence_end_mark:
            if word_index > 0:
                word_before_dot = words_array[word_index - 1]
                last_words.append(word_before_dot)
            return last_words


# Function to flatten a list of lists
def flat_map(fn, list_):
    result = []
    for item in list_:
        result.extend(fn(item))
    return result


class ImageWithText:
    def init(self, image: Image):
        self.image = image

    def get_last_word_of_every_sentence(self):
        # Extract text from the image
        image_text = pytesseract.image_to_string(self.image)

        # Format the text by inserting a space before each dot
        formatted_text = insert_space_before_dot(image_text)

        # Find the last word of each sentence
        last_words = find_word_before_dot(formatted_text)

        return last_words
import pytesseract
from PIL import Image


def insert_space_before_dot(text):
    text_with_space = text.replace('.', ' .')
    return text_with_space


def find_word_before_dot(text):
    words = text.split()
    last_words = []
    # print(words)
    for i in range(len(words)):
        if '.' in words[i] or '!' in words[i]:
            if i > 0:
                word_before_dot = words[i - 1]
                last_words.append(word_before_dot)
    return last_words


# Function to flatten a list of lists
def flat_map(f, xs):
    ys = []
    for x in xs:
        ys.extend(f(x))
    return ys


class ImageWithText:
    def __init__(self, image: Image):
        self.image = image

    def get_last_word_of_every_sentence(self):
        image_text = pytesseract.image_to_string(self.image)
        formatted_text = insert_space_before_dot(image_text)
        last_words = find_word_before_dot(formatted_text)
        return last_words
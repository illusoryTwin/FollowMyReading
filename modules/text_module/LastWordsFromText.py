class LastSentencesWords:
    """Class for retrieving last words from sentences in the text."""

    def __init__(self, string: str):
        """Initializes the class with a string."""
        self.string = string

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
                    word_before_mark = words_array[word_index - 1]
                    last_words_array.append(word_before_mark)

        return last_words_array

    def get_last_word_of_every_sentence(self):
        """
        Find the last word of each sentence in the text.
        """

        # Format the text by inserting a space before each punctuation mark
        formatted_text = self.insert_space_before_punct_mark(self.string)

        # Find the last word of each sentence
        last_words = self.find_word_before_punct_mark(formatted_text)

        return last_words


# # Instance 1 of LastSentencesWords
# text = "Hello! How are you? I hope you're doing well."
# ls_words = LastSentencesWords(text)
#
# # Retrieve the last words of each sentence
# last_words = ls_words.get_last_word_of_every_sentence()
#
# # Print the last words
# for word in last_words:
#     print(word)



# # Instance 2 of LastSentencesWords
# text = "Hello! How are you? I hope you're doing well."
# ls_words = LastSentencesWords(text)

# # Retrieve the last words of each sentence
# formatted_text = ls_words.insert_space_before_punct_mark(text)

# # Print the formatted text
# print(formatted_text)

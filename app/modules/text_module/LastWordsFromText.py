import re


class LastSentencesWords:
    """Class for retrieving last words from sentences in the text."""

    def __init__(self, string_list: list):
        """Initializes the class with a list of strings."""
        self.string_list = string_list

    @staticmethod
    def get_sentences(text):
        """
        Extract sentences from the text.
        Returns a list of strings, where each string represents a sentence from the text.
        """
        sentences = re.split('(?<=[.!?])', text)
        return sentences

    def get_last_word_of_every_sentence(self):
        """
        Find the last word of each sentence in the text.
        """
        last_words = []
        sentence_end_marks = ['.', '?', '!']

        for string in self.string_list:
            sentences = self.get_sentences(string)
            for sentence in sentences:
                words = sentence.split()
                if words:
                    last_word = words[-1]
                    # Remove any trailing punctuation signs
                    while last_word and last_word[-1] in sentence_end_marks:
                        last_word = last_word[:-1]
                    last_words.append(last_word)

        return last_words

class LanguageChecker:
    """Class to check the language and return specific results."""

    def __init__(self, language: str):
        """Initialize the class with a language."""
        self.language = language.lower()

    def get_lang_code(self, for_audio=False):
        """Return specific results based on the language."""
        if self.language == 'english' or self.language == 'eng':
            if for_audio:
                return "en"
            return 'eng'
        elif self.language == 'russian' or self.language == 'rus':
            if for_audio:
                return "ru"
            return 'rus'
        elif self.language == 'arabic' or self.language == 'ara':
            if for_audio:
                return "ar"
            return 'ara'
        else:
            return 'Unknown language'

class LanguageChecker:
    """Class to check the language and return specific results."""

    def __init__(self, language: str):
        """Initialize the class with a language."""
        self.language = language.lower()

    def get_lang_code(self, is_whisper: bool):
        """Return specific results based on the language."""
        if self.language == 'english' or self.language == 'eng':
            if is_whisper:
                return "en"
            return 'eng'
        elif self.language == 'russian' or self.language == 'rus':
            if is_whisper:
                return "ru"
            return 'rus'
        elif self.language == 'arabic' or self.language == 'ara':
            if is_whisper:
                return "ar"
            return 'ara'
        else:
            return 'Unknown language'

# pip install git+https://github.com/openai/whisper.git
# pip install pydub
# pip install Pillow

import whisper
from pydub import AudioSegment

class AudioTranscriptLangs:
    def __init__(self, audio_file_path: str):
        # Initialize class with audio file path
        self.audio_file_path = audio_file_path

    @staticmethod
    # Function to flatten a list of lists
    def flat_map(fn, list_):
        result = []
        # Apply function to every item in list, extending the result list
        for item in list_:
            result.extend(fn(item))
        return result

    def get_transcription(self, lang_code):
        """
        Transcribes audio into text
        :parameter audio_name - name of input audio
        :return transcription - the transcribed text
        """
        # Load the whisper model
        model = whisper.load_model('small')
        # Transcribe the audio file into words with timestamps. 16-bit floating point precision
        response = model.transcribe(self.audio_file_path, fp16=False, word_timestamps=True, language=lang_code)
        response_dic = response["segments"]

        transcription = []
        # Iterate over all segments, collecting all words in transcription
        for sentence in response_dic:
            for word in sentence['words']:
                transcription.append(word['word'])

        return transcription





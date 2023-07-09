#!pip install git+https://github.com/openai/whisper.git


# Import necessary libraries
import whisper  # For audio transcription


# Class for handling audio files with text
class AudioFileWithText:
    def __init__(self, audio_file_path: str):
        # Initialize the class with an audio file path
        self.audio_file_path = audio_file_path

    def get_timed_recognised_text(self):
        '''
        Transcribes audio into text utilizing "small" model
        :parameter audio_name - name of the input audio
        :return transcription - the transcribed text in the format: (word: timestamp)
        '''
        # Load the whisper model for audio transcription
        model = whisper.load_model('small')
        # Transcribe the audio file into words with timestamps using the model
        response = model.transcribe(self.audio_file_path, fp16=False, word_timestamps=True)
        response_dic = response["segments"]

        transcription = []
        # Iterate over all segments, collecting all words in the transcription
        for sentence in response_dic:
            for word in sentence['words']:
                transcription.append(word)

        return transcription

# # Example of usage
# audio = AudioFileWithText("часть 1.mp3")
# transcript = audio.get_timed_recognised_text()
# print(transcript)

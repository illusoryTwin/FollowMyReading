# pip install git+https://github.com/openai/whisper.git
# pip install pydub
# pip install Pillow

import whisper
from pydub import AudioSegment


class AudioFileWithTextLangs:
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

    def get_timed_recognised_text(self, lang_code):
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
                transcription.append(word)

        return transcription

    def get_words_from_audio(self, lang_code):
        """
        Transcribes audio into text
        :parameter audio_name - name of input audio
        :return words - a list of transcribed words
        """
        # Load the whisper model
        model = whisper.load_model('small')
        # Transcribe the audio file into words with timestamps. 16-bit floating point precision
        response = model.transcribe(self.audio_file_path, fp16=False, word_timestamps=True, language=lang_code)
        response_dic = response["segments"]

        words = []
        # Iterate over all segments, collecting all words in transcription
        for sentence in response_dic:
            for word in sentence['words']:
                words.append(word['word'])

        return words

    def get_end_time_of_each_sentence(self, last_words, lang_code: str):
        # Obtain timed transcriptions
        timed_recognised_text = self.get_timed_recognised_text(lang_code)
        mapping = []

        # For each 'last word', find matching transcriptions and store their end times
        for last_word in last_words:
            matching_transcriptions = []
            for transcription in timed_recognised_text:
                # print(last_word)
                # print("transcription", transcription)
                if last_word in transcription['word']:
                    matching_transcriptions.append(transcription['end'])
            mapping.append(matching_transcriptions)

        # Create list of end times for all words in mapping
        word_end_timestamps = [0]
        word_end_timestamps += self.flat_map(lambda lst: lst, mapping)
        return word_end_timestamps

    def split_audio_by_last_words(self, last_words, lang_code: str):
        """
        Splits the audio file into segments based on the 'last words' of sentences.
        """
        # Load audio file
        audio = AudioSegment.from_file(self.audio_file_path, format="mp3")

        segments = []
        # Obtain timestamps for all sentences' end times
        timestamps = self.get_end_time_of_each_sentence(last_words, lang_code)
        # No need to split by the very last word
        timestamps = timestamps[:-1]
        # print("timestamps", timestamps)
        # Iterate over all timestamps, splitting audio into segments
        for timestamp_index, timestamp in enumerate(timestamps):
            start_time = int(timestamp * 1000)
            if timestamp_index < len(timestamps) - 1:
                end_time = int(timestamps[timestamp_index + 1] * 1000)
            else:
                # For the last timestamp, use the end of the audio
                end_time = len(audio)

            # Create the audio segment
            segment = audio[start_time:end_time]
            segments.append(segment)
        return segments

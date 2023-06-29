from pydub import AudioSegment
import whisper

class AudioFileWithText:
    def __init__(self, audio_file_path: str):
        self.audio_file_path = audio_file_path

    def get_timed_recognised_text(self):
        # Load the whisper model
        model = whisper.load_model('small')
        result = model.transcribe(self.audio_file_path, fp16=False, word_timestamps=True)
        result = result["segments"][0]['words']
        return result

    def get_end_time_of_each_sentence(self, last_words):
        timed_recognised_text = self.get_timed_recognised_text()
        mapping = list(
            map(lambda last_word:
                list(
                    map(lambda filtered_transcription: (
                        filtered_transcription['end']),
                        filter(lambda transcription:
                               last_word in transcription['word'], timed_recognised_text))),
                last_words))
        final_timestamps = [0]
        final_timestamps += flat_map(lambda lst: lst, mapping)
        return final_timestamps

    def split_audio_by_last_words(self, last_words):
        audio = AudioSegment.from_file(self.audio_file_path, format="mp3")

        segments = []
        timestamps = self.get_end_time_of_each_sentence(last_words)
        for i, timestamp in enumerate(timestamps):
            start_time = int(timestamp * 1000)
            if i < len(timestamps) - 1:
                end_time = int(timestamps[i + 1] * 1000)
            else:
                end_time = len(audio)  # Set the last timestamp as the end of the audio

            segment = audio[start_time:end_time]
            segments.append(segment)
        return segments


def audio_transcribe(audio_path):
    # Load the whisper model
    model = whisper.load_model('small')
    result = model.transcribe(audio_path, fp16=False, word_timestamps=True)
    result = result["segments"][0]['words']
    return result

# Function to flatten a list of lists
def flat_map(f, xs):
    ys = []
    for x in xs:
        ys.extend(f(x))
    return ys
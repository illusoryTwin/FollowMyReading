import os
import shutil
from pydub import AudioSegment
import whisper


def audio_to_text(audio_name, cut_accuracy=150):
    """
    Recognizes the time boundaries of words from audio
    :parameter audio_name - name of input audio
    :parameter cut_accuracy - amount of ms to cut before and after word recognized. Adjust for slow/fast speech audios.
    """
    # able to change model (tiny/base/small/medium/large). The larger the model - the preciser transcription
    model = whisper.load_model('small')
    response = model.transcribe(audio_name, fp16=False, word_timestamps=True)
    segments_dic = response["segments"]
    response_dic = {}
    for sentence in segments_dic:
        for word in sentence['words']:
            msec_in_sec = 1000
            start_time = float(word['start']) * msec_in_sec - cut_accuracy
            end_time = float(word['end']) * msec_in_sec + cut_accuracy
            response_dic[word['word']] = [start_time, end_time]
    return response_dic

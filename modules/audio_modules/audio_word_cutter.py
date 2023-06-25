import os
import shutil
from pydub import AudioSegment
from modules.archive_modules.zip_archiver import add_file
import whisper


def audio_cutter(audio_name):
    model = whisper.load_model('small')
    response = model.transcribe(audio_name, fp16=False, word_timestamps=True)
    response_dic = response["segments"]
    n_of_chunk = 0
    audio_name_wout_format = audio_name[:-4]
    os.mkdir(audio_name_wout_format)
    for sentence in response_dic:
        for word in sentence['words']:
            msec_in_sec = 1000
            accuracy = 50
            start_time = float(word['start']) * msec_in_sec
            end_time = float(word['end']) * msec_in_sec + accuracy
            word_audio = AudioSegment.from_mp3(audio_name)
            cutted_word_audio = word_audio[start_time:end_time]
            out_file = audio_name_wout_format + "/chunk{}.mp3".format(n_of_chunk)
            cutted_word_audio.export(out_file, format="mp3")
            add_file(audio_name + ".zip", out_file)
            n_of_chunk += 1
    shutil.rmtree(audio_name_wout_format)
    return response_dic

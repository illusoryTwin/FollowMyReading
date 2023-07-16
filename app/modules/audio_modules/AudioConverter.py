import os

from pydub import AudioSegment


def convert_to_mp3(input_file_path, output_file_path):
    """
    The function to convert an audio-file to the .mp3 format
    """
    # Load the audio file
    audio = AudioSegment.from_file(input_file_path)

    # Export the audio as MP3
    audio.export(output_file_path, format='mp3')


def name_without_extension(file_path):
    return os.path.splitext(file_path)[0]

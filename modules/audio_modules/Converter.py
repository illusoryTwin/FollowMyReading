from pydub import AudioSegment

def convert_to_mp3(input_file_path, output_file_path):
    # Load the audio file
    audio = AudioSegment.from_file(input_file_path)

    # Export the audio as MP3
    audio.export(output_file_path, format='mp3')

# # Example usage
# input_file_path = 'russian.wav'
# output_file_path = 'output_audio2.mp3'
#
# convert_to_mp3(input_file_path, output_file_path)
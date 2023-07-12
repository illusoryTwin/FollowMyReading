from PIL import Image


def convert_to_jpg(input_file_path, output_file_path):
    '''
    Function converts an image file to the .jpeg format
    '''
    # Open the image file
    image = Image.open(input_file_path)

    # Convert and save the image as JPEG
    image.convert('RGB').save(output_file_path, 'JPEG')

# # Example usage
# input_file_path = 'russian1.png'
# output_file_path = 'output_image.jpg'
#
# convert_to_jpg(input_file_path, output_file_path)

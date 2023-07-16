import zipfile
from os.path import basename


def zip_add_file(archive_name, file_name):
    with zipfile.ZipFile(archive_name, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(file_name, basename(file_name.split("/")[-1]))
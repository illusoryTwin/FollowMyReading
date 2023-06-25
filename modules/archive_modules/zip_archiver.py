import zipfile


def add_file(archive_name, file_name):
    with zipfile.ZipFile(archive_name, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(file_name, arcname=file_name)

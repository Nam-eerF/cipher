import os
import pyAesCrypt
from pathlib import Path


def encrypt(file_path, password, delete_file=False):
    if Path(file_path).exists():
        file_path = Path(file_path).resolve()
        directory = Path(file_path).parent
        filename = Path(file_path).stem

        if Path(file_path).suffix == '.aes':
            return 'The file is encrypted', False

        decode_file = f'{Path(directory).joinpath(filename)}.aes'
        pyAesCrypt.encryptFile(file_path, decode_file, password)

        if delete_file:
            os.remove(file_path)
        return 'Success', True

    return 'No file', False


def decrypt(file_path, password, extension='.txt', delete_file=False):
    if Path(file_path).exists():
        directory = Path(file_path).parent
        filename = Path(file_path).stem

        if Path(file_path).suffix != '.aes':
            return 'Error extension', False

        extension = extension if extension[0] == '.' else f'.{extension}'

        encrypt_file = f'{Path(directory).joinpath(filename)}{extension}'
        pyAesCrypt.decryptFile(file_path, encrypt_file, password)

        if delete_file:
            os.remove(file_path)
        return 'Success', True

    return 'No file', False
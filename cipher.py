import os
import pyAesCrypt
from pathlib import Path


# Function of encrypting file
def encrypt(file_path, password, delete_file=False):
    # Check if file exists
    if Path(file_path).exists():
        file_path = Path(file_path).resolve()
        directory = Path(file_path).parent
        filename = Path(file_path).stem

        # Check if file isn't encrypted
        if Path(file_path).suffix == '.aes':
            return 'The file is encrypted', False

        # Encrypt the file
        decode_file = f'{Path(directory).joinpath(filename)}.aes'
        pyAesCrypt.encryptFile(file_path, decode_file, password)

        # Delete the file
        if delete_file:
            os.remove(file_path)
        return 'Success', True

    return 'No file', False


# Function of decrypting file
def decrypt(file_path, password, extension='.txt', delete_file=False):
    # Check if file exists
    if Path(file_path).exists():
        directory = Path(file_path).parent
        filename = Path(file_path).stem

        # Check if file is encrypted
        if Path(file_path).suffix != '.aes':
            return 'Error extension', False

        extension = extension if extension[0] == '.' else f'.{extension}'

        # Decrypt the file
        encrypt_file = f'{Path(directory).joinpath(filename)}{extension}'
        pyAesCrypt.decryptFile(file_path, encrypt_file, password)

        # Delete the file
        if delete_file:
            os.remove(file_path)
        return 'Success', True

    return 'No file', False

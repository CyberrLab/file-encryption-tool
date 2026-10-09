# File Encryption Tool

A Python cybersecurity project for encrypting and decrypting files using the Fernet symmetric encryption system from the `cryptography` library.

## Features

- Generates a Fernet encryption key.
- Encrypts files and saves them with the `.encrypted` extension.
- Decrypts encrypted files into separate `.decrypted` files.
- Reports errors for missing files, invalid file types, and incorrect keys or modified encrypted files.

## Technologies

- Python
- Cryptography library
- Fernet symmetric authenticated encryption

## Requirements

Python and the package listed in `requirements.txt`.

Install the dependency with:

`python -m pip install -r requirements.txt`

## How to Run

1. Open a terminal in the project folder.
2. Run:

   `python file_encryption.py`

3. Choose an option from the menu to generate a key, encrypt a file, decrypt a file, or exit.

## Security Notes

- Keep `secret.key` private and back it up securely.
- Never commit the encryption key to GitHub.
- Losing the key may make encrypted files unrecoverable.
- Use test files when learning and testing the program.

## Project Status

Completed beginner project. Encryption and decryption have been tested locally.
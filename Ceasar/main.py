import os

def generate_key():
    return os.urandom(1)[0] % 25 + 1


def encryption(message, key):
    result = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char

    return result


def decryption(message, key):
    return encryption(message, -key)


def enc_file(file_path, key):
    try:
        with open(file_path, 'r') as file:
            original = file.read()
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'existe pas. Création du fichier...")
        original = ""

    enc_message = encryption(original, key).upper()

    with open(file_path, 'w') as file:
        file.write(enc_message)

    return enc_message


def dec_file(file_path, key):
    with open(file_path, 'r') as file:
        enc_message = file.read()

    dec_message = decryption(enc_message, key)

    with open(file_path, 'w') as file:
        file.write(dec_message)

    return dec_message

key = generate_key()
file_path = 'message.txt'

enc = enc_file(file_path, key)
print(enc)
dec = dec_file(file_path, key)
print(dec)
import os
import getpass
import random
import json
from hashlib import pbkdf2_hmac


def save_seed(enc_seed, file_path='seed_config.json'):
    enc_seed_list = [int(byte) for byte in enc_seed]

    print(f'Saving seed : {enc_seed_list}')

    with open(file_path, 'w') as file:
        json.dump({"encrypted_seed": enc_seed_list}, file)


def load_seed(file_path='seed_config.json'):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return bytes(data.get("encrypted_seed", []))

    except FileNotFoundError:
        return None

    except json.JSONDecodeError:
        print("Error decoding JSON. Check the integrity of the file.")
        return None


def derive_key(password, salt, key_length=32):
    return pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, key_length)


def unlock_seed(enc_seed, password):
    salt = b'some_salt'
    key = derive_key(password, salt, 32)
    dec_seed = bytes([a ^ b for a, b in zip(enc_seed, key)])
    return dec_seed


def generate_key(seed, key_length):
    random.seed(seed)
    return bytes([random.randint(0, 255) for _ in range(key_length)])


def xor_encrypt(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    enc_data = bytes(([a ^ b for a, b in zip(plaintext, key)]))

    with open(output_file, 'wb') as file:
        file.write(enc_data)

    return enc_data


def xor_decrypt(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        cipher = file.read()

    dec_data = bytes([a ^ b for a, b in zip(cipher, key)])

    with open(output_file, 'wb') as file:
        file.write(dec_data)

    return dec_data

def verify_password(saved_enc_seed, entered_password):
    loaded_enc_seed = load_seed()

    if loaded_enc_seed:
        print('Encrypted seed loaded')
        dec_seed = unlock_seed(loaded_enc_seed, entered_password)

        return dec_seed == saved_enc_seed

    return False

if __name__ == '__main__':
    user_input = getpass.getpass("Please enter your password: ")
    loaded_enc_seed = load_seed()

    if loaded_enc_seed:
        print("Seed chiffrée chargée.")
        decrypted_seed = unlock_seed(loaded_enc_seed, user_input)

    else:
        print("No existing seed found. Creating a new one.")
        new_seed = os.urandom(32)  # Génère une nouvelle seed aléatoire
        save_seed(new_seed)
        decrypted_seed = new_seed

    key_length = 32

    key = generate_key(loaded_enc_seed, key_length)

    input = 'file1.txt'
    enc_file = 'file2.txt'
    dec_file = 'file3.txt'

    a = xor_encrypt(input, enc_file, key)
    print(a)

    b = xor_decrypt(enc_file, dec_file, key)
    print(b)
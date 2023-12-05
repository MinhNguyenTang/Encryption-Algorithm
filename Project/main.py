import base64
import secrets
from cryptography.fernet import Fernet

def generate_the_key():
    key_length = 32
    key = secrets.token_bytes(key_length)

    return key

def save_the_key(key, file='filekey.txt'):
    key_encoded = base64.b64encode(key).decode('utf-8')

    with open(file, 'w') as filekey:
        filekey.write(key_encoded)

def upload_the_key(file='filekey.txt'):
    with open(file, 'r') as filekey:
        key_encoded = filekey.read()

    key = base64.b64decode(key_encoded)

    return key

def encrypt_file(file_path, output_file_path):
    key = generate_the_key()
    save_the_key(key)

    fernet = Fernet(base64.b64encode(key).decode('utf-8'))

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(output_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"Résultat chiffrement : {encrypted}")

    return encrypted

def decrypt_file(file_path, output_file_path):
    key = upload_the_key()
    fernet = Fernet(base64.b64encode(key).decode('utf-8'))

    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(output_file_path, 'wb') as dec_file:
        dec_file.write(decrypted)

    print(f"Résultat déchiffrement : {decrypted}")

    return decrypted

#encrypt_file('pessimistic_poem.txt', 'pessimistic_poem.txt')
decrypt_file('pessimistic_poem.txt', 'pessimistic_poem.txt')
import hashlib
import random
import string
import codecs
import os
import base64
import secrets

file_path = 'C:/Users/33695/Desktop/Encryption-Algorithm/Project/nba.csv'

def open_file():
    with open(file_path, 'r') as file:
        file_content = file.read()
    print(file_content)
    return file_content

def write_file():
    with open(file_path, 'w') as file:
       file.write()
def open_filekey():
    key = write_filekey()
    with open('filekey.txt', 'r') as filekey:
        key = filekey.read()
    return key
def write_filekey():
    the_key= generate_the_key()
    iv = generate_random_iv()
    with open('filekey.txt', 'w') as filekey:
        key = filekey.write(the_key)
    return key

def get_the_key():
    combined_key = open_filekey()
    return combined_key

def hash_the_key():
    pass

def encrypt_file():
    pass
def generate_key_stream(key_length=32):
    key = secrets.token_bytes(key_length)
    key_encoded = base64.b64encode(key).decode('utf-8')
    return key_encoded
def generate_random_iv(blocksize=16):
    iv = secrets.token_bytes(blocksize)
    return bytes(iv)
def generate_the_key():
    key = generate_key_stream()
    iv = generate_random_iv()
    the_key = key + iv.hex()
    return the_key
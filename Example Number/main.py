def encrypt_number(number, key):
    # Simple modular arithmetic encryption
    encrypted_number = (number + key) % 256
    return encrypted_number

def decrypt_number(encrypted_number, key):
    # Simple modular arithmetic decryption
    decrypted_number = (encrypted_number - key) % 256
    return decrypted_number

# Example usage
secret_key = 42
original_number = 123

# Encrypt the number
encrypted_number = encrypt_number(original_number, secret_key)
print("Encrypted Number:", encrypted_number)

# Decrypt the number
decrypted_number = decrypt_number(encrypted_number, secret_key)
print("Decrypted Number:", decrypted_number)
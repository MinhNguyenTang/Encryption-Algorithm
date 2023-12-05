import os
import base64
import secrets

def generate_key(key_length=32):
    """Générer une clé aléatoire et l'encoder en base64."""
    key = secrets.token_bytes(key_length)
    key_encrypted = base64.b64encode(key).decode('utf-8')
    return key_encrypted

def encrypt_file(input_file, output_file, key):
    """Chiffre le contenu du fichier d'entrée et écrit le résultat dans le fichier de sortie."""
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    key_bytes = base64.b64decode(key)
    encrypted_data = bytes([a ^ b for a, b in zip(plaintext, key_bytes)])

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    """Déchiffre le contenu du fichier d'entrée et écrit le résultat dans le fichier de sortie."""
    with open(input_file, 'rb') as f:
        ciphertext = f.read()

    key_bytes = base64.b64decode(key)
    decrypted_data = bytes([a ^ b for a, b in zip(ciphertext, key_bytes)])

    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Exemple d'utilisation
if __name__ == "__main__":
    key = generate_key()

    input_file = "votre_fichier.txt"
    encrypted_file = "fichier_chiffre.txt"
    decrypted_file = "fichier_dechiffre.txt"

    encrypt_file(input_file, encrypted_file, key)
    decrypt_file(encrypted_file, decrypted_file, key)

    print("Opérations de chiffrement et de déchiffrement terminées avec succès.")
    print("Clé utilisée:", key)
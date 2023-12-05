import secrets
import base64

def generate_key(key_length=32):
    # Générer une clé aléatoire
    key = secrets.token_bytes(key_length)

    # Encoder la clé en base64
    key_encrypted = base64.b64encode(key).decode('utf-8')

    return key_encrypted

    # Exemple d'utilisation
key_encrypted = generate_key()
print("Key generated in base64:", key_encrypted)
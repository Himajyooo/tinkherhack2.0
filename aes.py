from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_aes(message):
    key = get_random_bytes(16)  # Generate a random key for AES-128
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return ciphertext.hex(), key.hex()

def decrypt_aes(encrypted_text, key):
    cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC)
    decrypted_message = unpad(cipher.decrypt(bytes.fromhex(encrypted_text)), AES.block_size)
    return decrypted_message.decode()

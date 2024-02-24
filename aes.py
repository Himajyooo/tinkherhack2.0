from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext, cipher.iv

def decrypt_message(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message

# Get user input for message
message = input("Enter the message to encrypt: ").encode()

# Generate a random key
key = get_random_bytes(16)  # 16 bytes for AES-128, 24 bytes for AES-192, 32 bytes for AES-256

# Encrypt the message
ciphertext, iv = encrypt_message(message, key)

print("\nOriginal message:", message.decode())
print("Encrypted ciphertext:", ciphertext.hex())

# Decrypt the message
decrypted_message = decrypt_message(ciphertext, key, iv)

print("Decrypted message:", decrypted_message.decode())
print('key=',key)

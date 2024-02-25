# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad, unpad
# import binascii

# # def encrypt_aes(message):
# #     key = get_random_bytes(16)  # Generate a random key for AES-128
# #     cipher = AES.new(key, AES.MODE_CBC)
# #     ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
# #     return ciphertext.hex(), key.hex()
# def encrypt_aes(message, key):
#     cipher = AES.new(key, AES.MODE_CBC)
#     ciphertext = cipher.encrypt(pad(message, AES.block_size))
#     return ciphertext, cipher.iv

# # def decrypt_aes(encrypted_text, key):
# #     cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC)
# #     decrypted_message = unpad(cipher.decrypt(bytes.fromhex(encrypted_text)), AES.block_size)
# #     return decrypted_message.decode()
# # def decrypt_aes(encrypted_text, key):
# #     try:
# #         cipher = AES.new(binascii.unhexlify(key), AES.MODE_CBC)
# #         decrypted_message = unpad(cipher.decrypt(binascii.unhexlify(encrypted_text)), AES.block_size)
# #         return decrypted_message.decode()
# #     except Exception as e:
# #         return str(e)
# def decrypt_aes(ciphertext, key,iv):
#     cipher = AES.new(key, AES.MODE_CBC,iv)
#     decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
#     return decrypted_message
# key = get_random_bytes(16)
# t,iv=encrypt_aes("helooo",key)
# print(decrypt_aes(t,key,iv))
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_aes(message, key):
    message = message.encode()
    
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext, cipher.iv

def decrypt_aes(ciphertext, key, iv):
    key = get_key()
    iv = get_iv()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(ciphertext)
    decrypted_message = unpad(decrypted_message, AES.block_size)
    return decrypted_message.decode()
# Generate a random key
key = get_random_bytes(16)  # 16 bytes for AES-128, 24 bytes for AES-192, 32 bytes for AES-256

# Generate a random IV
iv = get_random_bytes(16)

def get_key():
    return key

def get_iv():
    return iv
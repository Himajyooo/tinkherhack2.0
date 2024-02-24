def encrypt_caeser(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift the character by the specified amount
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Shift the character back by the specified amount
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            # Leave non-alphabetic characters unchanged
            decrypted_text += char
    return decrypted_text

def caesar_cipher_vowels_consonants(text, vowel_shift, consonant_shift):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    result = ""
    
    for char in text:
        if char.lower() in vowels:
            # Determine the shift direction (positive or negative)
            #shift_direction = 1 if char.islower() else -1
            # Calculate the new vowel
            new_vowel = vowels[(vowels.index(char.lower()) + vowel_shift ) % int(len(vowels)/2)]
            # Preserve the case
            new_vowel = new_vowel.upper() if char.isupper() else new_vowel
            result += new_vowel
        elif char.lower() in consonants:
            # Determine the shift direction (positive or negative)
            #shift_direction = 1 if char.islower() else -1
            # Calculate the new consonant
            new_consonant = consonants[(consonants.index(char.lower()) + consonant_shift) % int(len(consonants)/2)]
            # Preserve the case
            new_consonant = new_consonant.upper() if char.isupper() else new_consonant
            result += new_consonant
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

# Example usage
plaintext = "yu"
vowel_shift = 3
consonant_shift = 2
ciphertext = caesar_cipher_vowels_consonants(plaintext, vowel_shift, consonant_shift)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)

def caesar_cipher_vowels_consonants_decrypt(text, vowel_shift, consonant_shift):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    result = ""
    
    for char in text:
        if char.lower() in vowels:
            # Determine the shift direction (positive or negative)
            #shift_direction = 1 if char.islower() else -1
            # Calculate the new vowel
            new_vowel = vowels[(vowels.index(char.lower()) - vowel_shift) % int(len(vowels)/2)]
            # Preserve the case
            new_vowel = new_vowel.upper() if char.isupper() else new_vowel
            result += new_vowel
        elif char.lower() in consonants:
            # Determine the shift direction (positive or negative)
            #shift_direction = 1 if char.islower() else -1
            # Calculate the new consonant
            new_consonant = consonants[(consonants.index(char.lower()) - consonant_shift) % int(len(consonants)/2)]
            # Preserve the case
            new_consonant = new_consonant.upper() if char.isupper() else new_consonant
            result += new_consonant
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

print(caesar_cipher_vowels_consonants_decrypt(ciphertext, vowel_shift, consonant_shift))


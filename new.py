def consvow_encrypt(text, vowel_shift, consonant_shift):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    result = ""
    
    for char in text:
        if char.lower() in vowels:
            # Calculate the new vowel
            new_vowel = vowels[(vowels.index(char.lower()) + vowel_shift ) % int(len(vowels)/2)]
            new_vowel = new_vowel.upper() if char.isupper() else new_vowel
            result += new_vowel
        elif char.lower() in consonants:
            # Calculate the new consonant
            new_consonant = consonants[(consonants.index(char.lower()) + consonant_shift) % int(len(consonants)/2)]
            new_consonant = new_consonant.upper() if char.isupper() else new_consonant
            result += new_consonant
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def consvow_decrypt(text, vowel_shift, consonant_shift):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    result = ""
    
    for char in text:
        if char.lower() in vowels:
            # Calculate the new vowel
            new_vowel = vowels[(vowels.index(char.lower()) - vowel_shift) % int(len(vowels)/2)]
            new_vowel = new_vowel.upper() if char.isupper() else new_vowel
            result += new_vowel
        elif char.lower() in consonants:
            # Calculate the new consonant
            new_consonant = consonants[(consonants.index(char.lower()) - consonant_shift) % int(len(consonants)/2)]
            new_consonant = new_consonant.upper() if char.isupper() else new_consonant
            result += new_consonant
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


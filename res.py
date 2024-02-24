import random
import math

def generate_prime_number():
    
    while True:
        prime_candidate = random.randint(2**15, 2**16)
        if is_prime(prime_candidate):
            return prime_candidate

def is_prime(n, k=5):
    
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gcd(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keys():
    
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt_res(message, public_key):
    
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def decrypt_res(ciphertext, private_key):
    
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

def main():
    
    public_key, private_key = generate_keys()

    
    message = input("Enter the message to encrypt: ")

    
    encrypted_message = encrypt_res(message, public_key)
    print("Encrypted message:", encrypted_message)

    
    decrypted_message = decrypt_res(encrypted_message, private_key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()




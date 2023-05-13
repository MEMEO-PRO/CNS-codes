import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    def eea(a, b):
        if b == 0:
            return (1, 0, a)
        (x, y, d) = eea(b, a % b)
        return (y, x - (a // b) * y, d)

    (x, y, d) = eea(e, phi)
    if d == 1:
        return x % phi
    else:
        return None

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    n = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

# example usage:
p = 61
q = 53
public, private = generate_keypair(p, q)

print("Public key: ", public)
print("Private key: ", private)

message = input("Enter Plain text to encrypt and decrypt : ")
print("Original message: ", message)

encrypted_message = encrypt(public, message)
print("Encrypted message: ", encrypted_message)

decrypted_message = decrypt(private, encrypted_message)
print("Decrypted message: ", decrypted_message)


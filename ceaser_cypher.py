def caesar_cipher_encrypt(text, shift):
   
    result = ""
    for char in text:
        if char.islower():
            ascii_offset = ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        elif char.isupper():
            ascii_offset = ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def caesar_cipher_encrypt(text, shift):
    """
    Encrypts a given text using Caesar Cipher encryption.
    
    Args:
    - text (str): The input text to be encrypted.
    - shift (int): The integer shift value (between 0-25) for the cipher.
    
    Returns:
    - str: The encrypted text.
    """
    result = ""
    for char in text:
        if char.islower():
            ascii_offset = ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        elif char.isupper():
            ascii_offset = ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result


def caesar_cipher_decrypt(text, shift):
    """
    Decrypts a given text using Caesar Cipher decryption.
    
    Args:
    - text (str): The input text to be decrypted.
    - shift (int): The integer shift value (between 0-25) for the cipher.
    
    Returns:
    - str: The decrypted text.
    """
    result = ""
    for char in text:
        if char.islower():
            ascii_offset = ord('a')
            shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += shifted_char
        elif char.isupper():
            ascii_offset = ord('A')
            shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result



text = "NOTVERYSECURE"
shift = 7
encrypted_text = caesar_cipher_encrypt(text, shift)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

print("Original text: ", text)
print("Encrypted text: ", encrypted_text)
print("Decrypted text: ", decrypted_text)

text = "NOTVERYSECURE"
shift = 7
encrypted_text = caesar_cipher_encrypt(text, shift)

print("Original text: ", text)
print("Encrypted text: ", encrypted_text)

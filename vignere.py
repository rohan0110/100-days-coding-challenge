def vigenere_cipher_encrypt(plain_text, key):
    encrypted_text = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index]) - 65  # Calculate the shift amount for the current key character
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            key_index = (key_index + 1) % key_length
        else:
            encrypted_text += char
    return encrypted_text

# Take user input
plain_text = input("Enter the text to encrypt: ")
key = input("Enter the encryption key: ")

# Encrypt the text
encrypted_text = vigenere_cipher_encrypt(plain_text, key)

# Print the original text and the encrypted text
print("Original Text:", plain_text)
print("Encrypted Text:", encrypted_text)

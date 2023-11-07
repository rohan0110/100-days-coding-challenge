def additive_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def additive_cipher_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - key) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

# Take user input
text = input("Enter the text to encrypt: ")
key = 6

# Encrypt and decrypt the text
encrypted_text = additive_cipher_encrypt(text, key)
decrypted_text = additive_cipher_decrypt(encrypted_text, key)

# Print the original text and the decrypted text
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

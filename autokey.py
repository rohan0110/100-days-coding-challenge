def autokey_cipher_encrypt(text, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr(((ord(char) - 65 + ord(key[key_index]) - 65) % 26) + 65)
            else:
                encrypted_text += chr(((ord(char) - 97 + ord(key[key_index]) - 97) % 26) + 97)
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char
    return encrypted_text

def autokey_cipher_decrypt(text, key):
    decrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr(((ord(char) - ord(key[key_index]) + 26) % 26) + 65)
            else:
                decrypted_text += chr(((ord(char) - ord(key[key_index]) + 26) % 26) + 97)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char
    return decrypted_text

# Take user input
text = input("Enter the text to encrypt: ")
key = input("Enter the key(Character): ")

# Encrypt and decrypt the text
encrypted_text = autokey_cipher_encrypt(text, key)
decrypted_text = autokey_cipher_decrypt(encrypted_text, key)

# Print the original text and the decrypted text
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

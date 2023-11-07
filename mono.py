def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

# Take user input
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt and decrypt the text
encrypted_text = caesar_cipher_encrypt(text, shift)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

# Print the original text and the decrypted text
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

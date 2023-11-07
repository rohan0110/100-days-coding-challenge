def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_cipher_encrypt(text, key_a, key_b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr(((ord(char) - 65) * key_a + key_b) % 26 + 65)
            else:
                encrypted_text += chr(((ord(char) - 97) * key_a + key_b) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def affine_cipher_decrypt(text, key_a, key_b):
    decrypted_text = ""
    mod_inv = mod_inverse(key_a, 26)
    if mod_inv is None:
        return "Invalid key. 'a' must be chosen such that it is coprime with 26."
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr(((ord(char) - 65 - key_b) * mod_inv) % 26 + 65)
            else:
                decrypted_text += chr(((ord(char) - 97 - key_b) * mod_inv) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

# Take user input
text = input("Enter the text to encrypt: ")
key_a = int(input("Enter the key A value (an integer coprime with 26): "))
key_b = int(input("Enter the key B value (an integer): "))

# Encrypt and decrypt the text
encrypted_text = affine_cipher_encrypt(text, key_a, key_b)
decrypted_text = affine_cipher_decrypt(encrypted_text, key_a, key_b)

# Print the original text and the decrypted text
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

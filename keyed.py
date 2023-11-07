def keyed_transposition_cipher_encrypt(text, key):
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    sorted_indices = [index for index, _ in sorted_key]

    encrypted_text = ''
    for i in sorted_indices:
        encrypted_text += ''.join(text[i - 1::len(key)])

    return encrypted_text

# Example usage
text = "This is a test message for the keyed transposition cipher."
key = "45213"

encrypted_text = keyed_transposition_cipher_encrypt(text, key)
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)

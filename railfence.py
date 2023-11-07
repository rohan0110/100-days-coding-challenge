def rail_fence_cipher_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return ''.join(result)

# Take user input
text = input("Enter the text to encrypt: ")
key = int(input("Enter the key: "))

# Encrypt the text
encrypted_text = rail_fence_cipher_encrypt(text, key)

# Print the original text and the encrypted text
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)

import numpy as np

# Function to generate the key matrix
def generate_key_matrix(key, n):
    k = 0
    key_matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if k < len(key):
                key_matrix[i][j] = ord(key[k]) % 65
            else:
                key_matrix[i][j] = 0  # Filling the remaining space with zeros
            k += 1
    return key_matrix

# Function to encrypt the message
def hill_cipher_encrypt(message, key_matrix, n):
    message_vector = []

    for letter in message:
        message_vector.append(ord(letter) % 65)

    while len(message_vector) % n != 0:
        message_vector.append(23)  # 23 represents 'X'

    message_matrix = np.array(message_vector)
    message_matrix = np.reshape(message_matrix, (-1, n))

    encrypted_text = ""

    for row in message_matrix:
        row = np.transpose([row])
        result = np.dot(key_matrix, row) % 26
        for val in result:
            encrypted_text += chr(val.item() + 65)  # Convert the numpy scalar to an integer

    return encrypted_text

# Take user input
message = input("Enter the message to encrypt: ").upper()
key = input("Enter the key: ").upper()
n = int(input("Enter the size of the matrix: "))

key_matrix = generate_key_matrix(key, n)
encrypted_message = hill_cipher_encrypt(message, key_matrix, n)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)

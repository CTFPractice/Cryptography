import base64

ciphertext = input("Please input the ciphertext:")
plaintext = base64.b64decode(ciphertext)
print(plaintext)
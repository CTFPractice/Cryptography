import base64

ciphertext = input("Please input the ciphertext:")
plaintext = base64.b32decode(ciphertext)
print(plaintext)

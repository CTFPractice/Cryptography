Base32
===
## Decipher
### Online Tool
- [Base32 Decode](https://emn178.github.io/online-tools/base32_decode.html)

### Python
```
# base32_decode.py
import base64

ciphertext = input("Please input the ciphertext:")
plaintext = base64.b32decode(ciphertext)
print(plaintext)
```

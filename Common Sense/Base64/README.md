Base64
===
## Principle
Base64 由 64 個字元組成，包含 A-Za-z0-9+/。
![](https://i.imgur.com/eGMSXNF.png)

由於 2^6^=64，在計算時會先從 ascii 轉成 binary，在將 binary 分為每六個 bits 一組，從新轉回十進位引所值，再對照引所表將其轉換為 Base64編碼。
![](https://i.imgur.com/TaqnSOd.png)

如果轉化出來的 binary pattarn 不是六的倍數，會以 padding（補零）的方式，使其成為六的倍數，而最後 padding 的 bits，再編碼後會轉化成 = 或 ==，所以如果在密文的尾端看到 =，十之八九可能是 Base 編碼。
![](https://i.imgur.com/O1V6zJE.png)

## Decipher
### Online Tool
- [BASE64](https://www.base64decode.org/)
- [ASCII to Hex](https://www.asciitohex.com/)

### Python
```
# base64_decode.py
import base64

ciphertext = input("Please input the ciphertext:")
plaintext = base64.b64decode(ciphertext)
print(plaintext)
```

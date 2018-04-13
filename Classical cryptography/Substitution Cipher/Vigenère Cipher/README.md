Vigenère cipher
===
## Principle
透過交替的凱撒密碼進行加密。
1. 先選擇一把 key
2. 不斷重複 key 使其長度同於 plaintext
3. 利用查表法得到 ciphertext

![](https://i.imgur.com/Zmx2Kb8.png)

```
plaintext  : HELLOWORLD
key        : NCHUITNCHU
ciphertext : UGSFWPBTSX
```

## Decipher
### Online Tool
- [vigenere-cipher](https://www.dcode.fr/vigenere-cipher)
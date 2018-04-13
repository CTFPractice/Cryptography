Simple Substitution Cipher 簡易替換密碼
===
## Principle
將單一字母隨機對應，建立替換表，共有 26! 種可能性。傳統上會先把一個關鍵詞寫在字母表最前面，再刪去重複字母，這樣就能得到一個混合表。
```
key : NCHUIT
plaintext  : ABCDEFGHIJKLMNOPQRSTUVWXYZ 
ciphertext : NCHUITABDEFGJKLMOPQRSVWXYZ
```

## 特例
**Caesar Cipher 凱薩密碼**
以偏移的方法取得替換表。
```
plaintext  : ABCDEFGHIJKLMNOPQRSTUVWXYZ
ciphertext : DEFGHIJKLMNOPQRSTUVWXYZABC
```

**Atbash Cipher 阿特巴希密碼**
以逆轉的方式取得替換表。
```
plaintext  : ABCDEFGHIJKLMNOPQRSTUVWXYZ 
ciphertext : ZYXWVUTSRQPONMLKJIHGFEDCBA
```

## Cryptanalysis
**頻率分布**
Natural English 有它獨特的分布，所以可以計算密文中字母出現次數，嘗試破解密碼。
![](https://i.imgur.com/GELJZFy.png)
![](https://i.imgur.com/3eRnAsW.png)


## Decipher
### Online Tool
- [quipqiup](https://quipqiup.com/)

## Reference
- [Simple Substitution Cipher](http://practicalcryptography.com/ciphers/simple-substitution-cipher/)
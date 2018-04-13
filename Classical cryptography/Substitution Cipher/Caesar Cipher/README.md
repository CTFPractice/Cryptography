Caesar Cipher
===
## About
- 替換加密的一種
- 將明文所有字母在字母表上平移，轉換成密文
![](https://i.imgur.com/1AItQLc.png)

## Decipher
### Cryptanalysis
密鑰的樣本數非常小，可以利用遍歷直接暴力破解。

### Online Tool
- [Robert Eisele](http://www.xarg.org/tools/caesar-cipher/)
- [PLANETCALC](https://planetcalc.com/1434/)

### Linux Command
```
$ echo 'CTF{hello_world}' | tr x-za-w a-z	# encrypt
$ echo 'CTF{khoor_zruog}' | tr a-z x-za-w	# decrypt
```

### Python
```
# caesar_decode.py
ciphertext = input("Please input ciphertext:")
x = ciphertext[0]

for keyspace in range(-(ord(x)-65),91-ord(x)):
	for i in ciphertext:
		if (ord(i)>=65 and ord(i)<=90):
			print(chr((ord(i)+keyspace-65)%26+65), end="")
		elif (ord(i)>=97 and ord(i)<=122):
			print(chr((ord(i)+keyspace-97)%26+97), end="")
		else:
			print(i, end="")
	print()
```

## Reference
- [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [ROT13](https://zh.wikipedia.org/wiki/ROT13)
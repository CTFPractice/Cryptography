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
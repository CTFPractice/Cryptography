

ciphertext = input("Please input ciphertext:")
caesar1 = "abcdefghijklmnopqrstuvwxyz"
caesar2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caesar3 = "0123456789"

for k in range(1,26+1):
	for i in range(0,len(ciphertext)):
		for j in range(0,26):
			if(ciphertext[i]==caesar1[j]):
				print(caesar1[(j+k)%len(caesar1)], end="")
			elif(ciphertext[i]==caesar2[j]):
				print(caesar2[(j+k)%len(caesar2)], end="")
		for j in range(0,9):
			if(ciphertext[i]==caesar3[j]):
				print(caesar3[(j+k)%len(caesar3)], end="")
	print()

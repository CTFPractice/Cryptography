lstr="""e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA"""

for p in range(127): 
	str1 = ''
	for i in lstr:
		temp = chr((ord(i)+p)%127)
		if 32<ord(temp)<127:
			str1 = str1 + temp
			feel = 1
		else:
			feel = 0
			break
	if feel == 1:
		print(str1)
import sys

# Prepared alphabet for Caesar Cipher. Can be changed.
caesaralpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def caesar(input_string, rot):
	strFileInp = open(sys.argv[2], 'rb')
	out = ""
	strInp = strFileInp.read().decode("utf-8").rstrip("\n")

if sys.argv[1] == "all":
    for i in range(1,len(caesaralpha)):
        out += "ROT " + str(i) + ": " + caesar(strInp, i) + "\n"
else:
    out = "ROT " + sys.argv[1] + ": " + caesar(strInp, sys.argv[1])
out = out.encode("utf-8")

print("Output: " + out.decode("utf-8"))
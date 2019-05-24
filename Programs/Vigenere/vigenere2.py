import sys

#
#
#

alphabet = [
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'0','1','2','3','4','5','6','7','8','9'
]

def encrypt(plain, key):
	global alphabet
	cipher = ""
	i = 0
	j = 0
	k = 0
	found = False
	while (i < len(plain)):
		for c in range(len(alphabet)):
			if key[i%len(key)] == alphabet[c]:
				found = True
				k = c
				break
		cipherAlphabet = alphabet[c:] + alphabet[:c]
		if found == True:
			for C in range(len(alphabet)):
				if plain[i] == alphabet[C]:
					cipher += cipherAlphabet[C]
					j += 1
					break
		i += 1
	return cipher

def decrypt(cipher, key):
	global alphabet
	plain = ""
	i = 0
	j = 0
	k = 0
	found = False
	while (i < len(cipher)):
		for c in range(len(alphabet)):
			if key[i%len(key)] == alphabet[c]:
				found = True
				k = c
				break
		cipherAlphabet = alphabet[c:] + alphabet[:c]
		if found == True:
			for C in range(len(cipherAlphabet)):
				if cipher[i] == cipherAlphabet[C]:
					plain += alphabet[C]
					j += 1
					break
		i += 1
	return plain

def keymod(key):
	str = ""
	for i in range (len(key)):
		str += key[i]
	return str

if (__name__ == "__main__"):
	args = sys.argv
	if (len(args) > 2):
		key = keymod(args[2])
		if (args[1] == "-e"):
			print encrypt(raw_input(), key)
		else:
			print decrypt(raw_input(), key)
	else:
		print "you typed it wrong"

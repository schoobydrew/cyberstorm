def decode(bitlength=8, message):
	return ''.join(chr(int(s[i*bitlength:i*bitlength+bitlength],2)) for i in range(len(message)//bitlength))
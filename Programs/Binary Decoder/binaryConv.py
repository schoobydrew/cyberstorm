def decode(message,bitlength=8):
	return ''.join(chr(int(message[i*bitlength:i*bitlength+bitlength],2)) for i in range(len(message)//bitlength))


if __name__ == '__main__':
	message = input('Input a Binary message:\n')
	if (len(message)%7 == 0) and (len(message)%8 ==0):
		print(decode(message))
		print(decode(message,7))
	elif (len(message)%7 == 0):
		print(decode(message,7))
	elif (len(message)%8 == 0):
		print(decode(message))
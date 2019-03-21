# by: Team Persia

# github: https://github.com/schoobydrew/cyberstorm
# located in the Programs folder, then the folder name Binary Decoder

import sys

# Decoder Function
# Input: int bitNum - 7 or 8 depending on if message is in 7 or 8 bit ASCII
#	 string encodedMsg - the message in binary
# Output: a decoded message
def decode(bitNum, encodedMsg):
	# for the length of the encodedMsg, decode 7 or 8 bits at a time
	i = 0
	asciiCode = 0
	decodedMessage = ""
	currentbits = 0
	while (i < len(encodedMsg)):
		# break into a bit word of correct length
		currentBits = encodedMsg[i:i+bitNum]
		# translate binary to decimal ASCII code
		asciiCode = int(currentBits, 2)
		# if a backspace, delete last character in message string
		if (len(decodedMessage) != 0 and asciiCode == 8):
			decodedMessage = decodedMessage[:-1]
		# otherwise add character to message string
		decodedMessage += chr(asciiCode)
		i += bitNum
	# return decoded message
	return decodedMessage


# Main Function
if (__name__ == "__main__"):
	# retrieve a string from stdin
	binaryMessage = raw_input()
	# if length of string divisble by 7
	if (len(binaryMessage)%7 == 0):
		# call decode using 7 as bitNum
		print decode(7, binaryMessage)
	# if length of string divisible by 8
	if (len(binaryMessage)%8 == 0):
		# call decode using 8 as bitNum
		print decode(8, binaryMessage)

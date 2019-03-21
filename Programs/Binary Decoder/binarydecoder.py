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
		# translate the 7 or 8 bits into a character
		# if a backspace, delete last character in message string
		# otherwise add character to message string
	# return decoded message

# Main Function
	# retrieve a string from stdin
	# if length of string divisble by 7,
	# call decode using 7 as bitNum
	# if 8 length of string divisible by 8,
	# call decode using 8 as bitNum
	# print decoded message

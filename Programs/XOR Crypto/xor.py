#Team - Persians
#github.com/schoobydrew/cyberstorm
import sys
keyfile = "file3"
def runXOR(text, key):
    xorText = ''
    for i in range(len(text)):
        j = text[i]
        k = key[i%len(key)]
        bitwise = (ord(j) ^ ord(k))
        xorText += chr(bitwise)
    return xorText
if (__name__ == "__main__"):
    #get text from stdin
    input = sys.stdin.read()
    #get key from hardcoded key file
    key = open(keyfile, "r").read()
    print runXOR(input, key)

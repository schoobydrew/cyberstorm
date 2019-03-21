#by: Team Persia
#
#github: https://github.com/schoobydrew/cyberstorm
import sys
def encrypt(plain, key):
    cipher = ""
    i = 0
    j = 0
    while (i < len(plain)):
        x = ord(plain[i])
        if (plain[i].isalpha()):
            if plain[i].isupper():
                x = x-ord('A')
            else:
                x = x-ord('a')
            x = (x + ord(key[j%len(key)])-ord('a'))%26
            if plain[i].isupper():
                x = x + ord('A')
            else:
                x = x + ord('a')
            j += 1
        cipher += chr(x)
        i += 1
    return cipher
def decrypt(cipher, key):
    plain = ""
    i = 0
    j = 0
    while (i < len(cipher)):
        x = ord(cipher[i])
        if (cipher[i].isalpha()):
            if cipher[i].isupper():
                x = x-ord('A')
            else:
                x = x-ord('a')
            x = (x - ord(key[j%len(key)]) + ord('a'))%26
            if cipher[i].isupper():
                x = x + ord('A')
            else:
                x = x + ord('a')
            j += 1
        plain += chr(x)
        i += 1
    return plain
def keymod(key):
    key = key.lower()
    key = key.replace(" ", "")
    str = ""
    for i in range(len(key)):
        if (key[i].isalpha()):
            str += key[i]
    key = str
    return key
if (__name__ == "__main__" ):
    args = sys.argv
    if (len(args) > 2):
        if (args[1].lower() == "-e"):
            crypto = True
        if (args[1].lower() == "-d"):
            crypto = False
        key = keymod(args[2])
        while (True):
            if (crypto):
                print encrypt(raw_input(), key)
            else:
                print decrypt(raw_input(), key)
    else:
        print "usage:"
        print "encryption>",
        print "python -e {your key}"
        print "decryption>",
        print "python -d {your key}"

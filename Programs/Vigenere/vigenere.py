#by: Team Persia
#
#github: https://github.com/schoobydrew/cyberstorm
import sys
#encryption function
#parameters: plaintext string, key string
#returns cipher text as string
def encrypt(plain, key):
    cipher = ""
    i = 0
    j = 0
    #increment i (index for plaintext) and j (index for cipher)
    while (i < len(plain)):
        x = ord(plain[i])
        if (plain[i].isalpha()):
            if plain[i].isupper():
                x = x-ord('A')
            else:
                x = x-ord('a')
            #get letters in terms of alphabet not ascii using modular arithmetic (mod 26) and retain case
            x = (x + ord(key[j%len(key)])-ord('a'))%26
            #get letters in terms of corresponding ascii value
            if plain[i].isupper():
                x = x + ord('A')
            else:
                x = x + ord('a')
            #only incremements to next key letter if we actually encrypt something i.e. a space is not encrypted
            j += 1
        #append new cipher letter in ascii to cipher text
        cipher += chr(x)
        #increment to next plaintext letter
        i += 1
    return cipher
#decryption function
#parameters: ciphertext string, key string
#returns plaintext text as string
def decrypt(cipher, key):
    plain = ""
    i = 0
    j = 0
    #increment i (index for plaintext) and j (index for cipher)
    while (i < len(cipher)):
        x = ord(cipher[i])
        if (cipher[i].isalpha()):
            if cipher[i].isupper():
                x = x-ord('A')
            else:
                x = x-ord('a')
            #get letters in terms of alphabet not ascii using modular arithmetic (mod 26) and retain case
            x = (x - ord(key[j%len(key)]) + ord('a'))%26
            #get letters in terms of corresponding ascii value
            if cipher[i].isupper():
                x = x + ord('A')
            else:
                x = x + ord('a')
            #only incremements to next key letter if we actually decrypt something i.e. a space is not decrypted
            j += 1
        #append new cipher letter in ascii to cipher text
        plain += chr(x)
        #increment to next plaintext letter
        i += 1
    return plain
#modifies key string for use by program
#parameters: key string
#returns: key string
def keymod(key):
    #only care about the actual letter (mod 26) later so case does not matter 
    key = key.lower()
    #only care about letters, anything else will be removed from key
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

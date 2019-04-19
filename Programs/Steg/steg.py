#Team Persians
#github.com/schoobydrew/cyberstorm
import sys
#globals
sentinel = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
BIT = False
BYTE = False
OFFSET = 0
INTERVAL = 0
Left = False
STEG = False
RETRIEVE = False
WRAPPER = ""
HIDDEN = ""
#functions
def doSteg():
    return object
def doRetrieve():
    return object
#main
if (__name__ == "__main__" ):
    for arg in sys.argv[1:]:
        if (arg[1] == "b"):
            BIT = True
            #sets to bit mode
        if (arg[1] == "B"):
            BYTE = True
            #sets to byte mode
        if (arg[1] == "s"):
            STEG = True
            #sets to encoding mode
        if (arg[1] == "r"):
            RETRIEVE = True
            #sets to decoding mode
        if (arg[1] == "o"):
            OFFSET = int(arg[2:])
            #sets the offset
        if (arg[1] == "i"):
            INTERVAL = int(arg[2:])
            #sets the interval
        if (arg[1] == "w"):
            WRAPPER = arg[2:]
            #wrapper file
        if (arg[1] == "h"):
            HIDDEN = arg[2:]
            #sets the hidden file
        if (arg[1] == "e"):
            LEFT = True
            #sets left to right -> right to left
    if (BIT and BYTE):
        print "Cannot use both bit and byte method"
        exit()
    if (STEG and RETRIEVE):
        print "Cannot both STEG and retrieve data"
        exit()
    if (WRAPPER == ""):
        print "Need to specify a wrapper file"
        exit()
    if (STEG and (HIDDEN == "")):
        print "Need a file to steg"
        exit()
    if (STEG):
        print doSteg()
    elif (RETRIEVE):
        print doRetrieve()

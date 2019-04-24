#Team Persians
#github.com/schoobydrew/cyberstorm
import sys
#globals
sentinel = [chr(0x0),chr(0xFF),chr(0x0),chr(0x0),chr(0xFF),chr(0x0)]
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
def printFile(arr):
    for x in arr:
        print x
def getFileData(fileName):
    data = open(fileName, "rb").read()
    return data
def doSteg():
    return object
def doRetrieve():
    publicFile = getFileData(WRAPPER)
    hiddenFile = []
    while (sentinel != hiddenFile[-len(sentinel):]):
        if (BIT):
            pass
        elif (BYTE):
            hiddenFile.append(chr(publicFile[OFFSET]))
            OFFSET += INTERVAL
    hiddenFile = hiddenFile[:-len(sentinel)]
    return hiddenFile
#main
if (__name__ == "__main__"):
    for arg in sys.argv[1:]:
        if (arg[1] == "b"):
            BIT = True
            print "BIT: {}".format(BIT)
            #sets to bit mode
        if (arg[1] == "B"):
            BYTE = True
            print "BYTE: {}".format(BYTE)
            #sets to byte mode
        if (arg[1] == "s"):
            STEG = True
            print "STEG: {}".format(STEG)
            #sets to encoding mode
        if (arg[1] == "r"):
            RETRIEVE = True
            print "RETREIVE: {}".format(RETRIEVE)
            #sets to decoding mode
        if (arg[1] == "o"):
            OFFSET = int(arg[2:])
            print "OFFSET: {}".format(OFFSET)
            #sets the offset
        if (arg[1] == "i"):
            INTERVAL = int(arg[2:])
            print "INTERVAL: {}".format(INTERVAL)
            #sets the interval
        if (arg[1] == "w"):
            WRAPPER = arg[2:]
            print "WRAPPER: {}".format(WRAPPER)
            #wrapper file
        if (arg[1] == "h"):
            print "HIDDEN: {}".format(HIDDEN)
            HIDDEN = arg[2:]
            #sets the hidden file
        if (arg[1] == "?"):
            LEFT = True
            print "Right>Left: {}".format(LEFT)
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
        hiddenFile = doRetrieve()
        printFile(hiddenFile)

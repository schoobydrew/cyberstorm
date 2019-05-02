import sys
from binascii import hexlify

##### Global variables #####

METHOD = ""
ACTION = ""
OFFSET = 1
INTERVAL = 1
WRAPPER = ""
HIDDEN = ""
ENDIAN = ""
sentinel = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
#storage Function
def store():
    global sentinel, OFFSET, INTERVAL
    storage = open(WRAPPER, "rb")
    hideFile = open(HIDDEN, "rb")
    W = bytearray(storage.read())
    H = bytearray(hideFile.read())
    if (METHOD == "B"):
        i = 0
        while (i < len(H)):
            W[OFFSET] = H[i]
            OFFSET += INTERVAL
            i += 1
        i = 0
        while i < len(sentinel):
            W[OFFSET] = sentinel[i]
            OFFSET += INTERVAL
            i += 1
        return ''.join(W)
    if (METHOD == "b"):
        i = 0
        j = 0
        while (j < len(H)):
            for k in range(0, 8):
                W[i] &= 11111110
                W[i] |= ((H[j] & 10000000) >> 7)
                H[j] <<= 1
                i += INTERVAL
            j += 1
        return ''.join(W)

#retrieve Function
def retrieve():
    global sentinel
    source = open(WRAPPER, "rb")
    i = 0
    data = []
    bytes = 0
    dataSet = ""
    if (METHOD == "B"):
        temp = source.read(1)
        while (temp != "" and data != sentinel):
            if (bytes == OFFSET + i*INTERVAL):
                if (len(data) == len(sentinel)):
                    data = data[1:]
                data.append(ord(temp))
                dataSet += temp
                i += 1
            bytes += 1
            temp = source.read(1)
        source.close()
        return dataSet
    if (METHOD == "b"):
        temp = source.read(1)
        byte = ''
        while (temp != "" and data != sentinel):
            if (bytes == OFFSET + i*8*INTERVAL + len(byte)*INTERVAL):
                temp = bin(ord(temp))[2:]
                #im pretty sure that endian will determine how we append bits to byte
                ##if im the program works fine without endian
                if (ENDIAN):
                    byte = temp[len(temp)-1] + byte
                else:
                    byte += temp[len(temp)-1]
                if (len(byte) == 8):
                    if (len(data) == len(sentinel)):
                        data = data[1:]
                    data.append(int(byte, 2))
                    dataSet += chr(int(byte, 2))
                    byte = ""
                    i += 1
            bytes += 1
            temp = source.read(1)
        return dataSet
for arg in sys.argv[1:]:
        if ((arg[1] == "b") or (arg[1] == "B")):
            METHOD = arg[1]
            #print "METHOD: {}".format(METHOD)
            #sets to bit mode
        if (arg[1] == "s") or (arg[1] == "r"):
            ACTION = arg[1]
            #print "Action: {}".format(ACTION)
            #sets to encoding mode or storage mode
        if (arg[1] == "o"):
            OFFSET = int(arg[2:])
            #print "OFFSET: {}".format(OFFSET)
            #sets the offset
        if (arg[1] == "i"):
            INTERVAL = int(arg[2:])
            #print "INTERVAL: {}".format(INTERVAL)
            #sets the interval
        if (arg[1] == "w"):
            WRAPPER = arg[2:]
            #print "WRAPPER: {}".format(WRAPPER)
            #wrapper file
        if (arg[1] == "h"):
            #print "HIDDEN: {}".format(HIDDEN)
            HIDDEN = arg[2:]
            #sets the hidden file
        if (arg[1] == "e"):
            ENDIAN = arg[1]
if (ACTION == 'r'):
    print retrieve()
elif (ACTION == 's'):
    print store()

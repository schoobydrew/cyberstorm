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
    global sentinel, HIDDEN, WRAPPER
    inc = 0
    hiddenBin = []
    storage = []
    hide = open(HIDDEN, "rb")
    temp = hide.read(1)
    while(temp != ""):
        hiddenBin.append(ord(temp))
        temp = hide.read(1)
    for sent in sentinel:
        hiddenBin.append(sent)
    store = open(WRAPPER, "rb")
    temp = store.read(1)
    while(temp != ""):
        storage.append(ord(temp))
        temp = store.read(1)
    for H in hiddenBin:
        if (METHOD == "B"):
            storage[OFFSET+INTERVAL*inc] = H
            inc += 1
        elif (METHOD == "b"):
            for k in range(8):
                storage[OFFSET+INTERVAL*inc] &= 0b11111110
                storage[OFFSET+INTERVAL*inc] |= ((H & 0b10000000) >> 7)
                H <<= 1
                inc += 1
    dataSet = ""
    for i in storage:
        dataSet += chr(i)
    return dataSet
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
        byte = 0
        byteL = 0
        while ((temp != "") and (data != sentinel)):
            if (bytes == OFFSET + i*8*INTERVAL + byteL*INTERVAL):
                temp = ord(temp)
                #im pretty sure that endian will determine how we append bits to byte
                ##if im wrong the program works fine without endian
                if (ENDIAN):
                    byte >>= 1
                    temp &= 1
                    temp << 7
                    byte |= temp
                else:
                    byte <<= 1
                    byte |= (temp & 1)
                byteL += 1
                if (byteL == 8):
                    if (len(data) == len(sentinel)):
                        data = data[1:]
                    data.append(byte)
                    dataSet += chr(byte)
                    byte = 0
                    byteL = 0
                    i += 1
            bytes += 1
            temp = source.read(1)
        source.close()
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
if (ACTION == "r"):
    print retrieve()
elif (ACTION == "s"):
    print store()

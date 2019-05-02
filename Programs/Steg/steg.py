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
#retrieve Function
def retrieve(METHOD, OFFSET, INTERVAL, WRAPPER):
    source = open(WRAPPER, "rb")
    i = 0
    data = []
    bytes = 0
    dataSet = ""
    if (METHOD == "B"):
        temp = source.read(1)
        while (temp != "" and sentinel != data):
            if (bytes == OFFSET + i*INTERVAL):
                if (len(data) == len(sentinel)):
                    data.pop(0)
                data.append(ord(temp))
                dataSet += temp
                i += 1
            bytes += 1
            temp = source.read(1)
        source.close()
        return dataSet
    if (METHOD == "b"):
        pass
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
    print retrieve(METHOD, OFFSET, INTERVAL, WRAPPER)
elif (ACTION == 's'):
    store(METHOD, OFFSET, INTERVAL, WRAPPER, HIDDEN)

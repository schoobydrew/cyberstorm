import sys
from binascii import hexlify

##### Global variables #####

METHOD = ""
ACTION = ""
OFFSET = 1
INTERVAL = 1
WRAPPER = ""
HIDDEN = ""


def retrieve():
    # open the file and save the contents into an array
    with open(WRAPPER, 'rb') as f:
        contents = f.read()

    i = OFFSET
    output = ''
    # Byte method
    if (METHOD == 'B'):
        while (i < len(contents)):
            output += contents[i]
            # check to see if sentinal values have been found
            if (len(output) >= 12):
                if (hexlify(output[-6:]) == "00ff0000ff00"):
                    # print the output without the sentinal values
                    print output[:-6]
                    break
            i += INTERVAL

    # bit method
    elif (METHOD == 'b'):
        print bin(int(hexlify(contents[i]), 16))[2:].zfill(8)
        while (i < len(contents)):
            #output += (contents[i] & 1)
            i += INTERVAL

def store():
    pass



if (__name__ == "__main__"):
    # obtain command line arguments  
    args = sys.argv
    # store method
    METHOD = args[1]
    METHOD = METHOD[1:]
    # store action
    ACTION = args[2]
    ACTION = ACTION[1:]
    # store offset
    OFFSET = args[3]
    OFFSET = int(OFFSET[2:])
    # store optional interval value
    if ('-i' in args[4]):
        INTERVAL = args[4]
        INTERVAL = int(INTERVAL[2:])
    else:
        # store wrapper file
        WRAPPER = args[4]
        WRAPPER = WRAPPER[2:]
    # at this point, if no optional arguments are used,
    # then there could no longer be any arguments left
    if (len(args) >= 6):
        if ('-w' in args[5]):
            # store wrapper file
            WRAPPER = args[5]
            WRAPPER = WRAPPER[2:]
        else:
            # store optional hidden file
            HIDDEN = args[5]
            HIDDEN = args[2:]
    if (len(args) == 7):
        # store optional hidden file
        HIDDEN = args[6]
        HIDDEN = HIDDEN[2:]
    
    if (ACTION == 'r'):
        retrieve()
    elif (ACTION == 's'):
        store()



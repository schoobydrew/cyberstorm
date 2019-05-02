import sys

#initialize variables
argMethod = ''
argStoreRetrieve = ''
argInterval = 0
argOffset = 0
argWrapperFile = ''
argHiddenFile = ''
sentinel = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

#Set input to be assigned to correct variable
try:
    argMethod = sys.argv[1]
    argStoreRetrieve = sys.argv[2]
    argOffset = sys.argv[3][2:]
    argInterval = sys.argv[4][2:]
    argWrapperFile = sys.argv[5][2:]
    if(argStoreRetrieve == '-s'):
        argHiddenFile = sys.argv[6][2:]
except:
    print "This is not the correct form try and follow '-(bB) -(rs) -o<val> -i<val> -(wrapper file) -(hidden file) > (outputfile)'"
    sys.exit()

#Function for storing stegged image
def store(method, offset, interval, wrapperFile, hiddenFile):
    global sentinel
    i = 0
    hiddenBin = []
    storage = []

    #Open hidden image file so you can bull the bytes and put them in an array
    image = open(hiddenFile, 'rb')
    pixValue = image.read(1)

    #until it reaches the end of the hidden file take each byte of the image, convert it to binary, and put it into the array.
    while(pixValue != ""):
        hiddenBin.append(format(ord(pixValue), '08b')) #Convert to ascii value then to binary format of '00000000'
        pixValue = image.read(1)

    #Add sentinel bytes to the array
    for sent in sentinel:
        hiddenBin.append(format(ord(chr(sent)), '08b'))

    #Take all of the bytes of the wrapper image and store them into an array
    image = open(wrapperFile, 'rb')
    pixValue = image.read(1)
    while(pixValue != ""):
        storage.append(format(ord(pixValue), '08b'))
        pixValue = image.read(1)

    #Cycle through each byte of the hidden file
    for j in hiddenBin:

        #If it is the byte mode replace each byte for the interval with a byte of the hidden file
        if(method == '-B'):
            storage[offset+interval*i] = j
            i += 1

        #If it is bit mode then replace the least signimicant bit of each byte of the wrapper file with a bit from the hidden file
        else:
            #Need to cycle through the byte
            for k in j:
                #start by ANDing the storage byte so the last bit is equal to 0
                storage[offset+interval*i] = format((int(storage[offset+interval*i], 2) & int('11111110', 2)), '08b')

                #Next OR the storage byte with the ANDed version of the hidden bit going from left to right.
                #It takes the most signimicant bit of the hidden byte and shifts it the the furthest point right.
                storage[offset+interval*i] = format(int(storage[offset+interval*i], 2) | ((int(j, 2) & int('10000000', 2)) >> 7), '08b')

                #Shift the hidden bit one to the left so the program can take the next bit on the far left
                j = format((int(j, 2) << 1), '08b')
                i += 1

    #Write to standard output
    for byte in storage:
        sys.stdout.write(chr(int(byte, 2)))

#Function when retrieving stegged message
def retrieve(method, offset, interval, wrapperFile):
    global sentinel
    #open image
    image = open(wrapperFile, 'rb')

    #initialize variables
    i = 0
    storage = []
    byte_count = 0

    #If retrieving in bit mode
    if(method == '-b'):
        pixValue = image.read(1) #Read byte
        cur_byte = ''

        #Continue reading bytes until no more message or you reach the seninel
        while (pixValue != "" and sentinel != storage):

            #Are we on a least significant bit
            if (byte_count == offset + i*8*interval + len(cur_byte)*interval):
                pixValue = bin(ord(pixValue))[2:]
                cur_byte += pixValue[len(pixValue) - 1] #Take lest significant byte and add it to the current byte

                #Have we reach a full byte
                if (len(cur_byte) == 8):
                    #If storage checking for the sentinel is the same size as the sentinel then get rid of the index 0
                    if(len(storage) == len(sentinel)):
                        storage.pop(0)
                    storage.append(int(cur_byte, 2))

                    sys.stdout.write(chr(int(cur_byte, 2))) #write byte to output

                    #reset cur_byte
                    cur_byte = ''
                    i += 1

            byte_count += 1
            pixValue = image.read(1) #Read again
    else:
        #Retrieve in Byte more
        pixValue = image.read(1)

        #Keep cycling through unti reach sentinel or end of image
        while (pixValue != "" and sentinel != storage):

            #If current byte is a byte in interval
            if (byte_count == offset + i*interval):
                if(len(storage) == len(sentinel)):
                    storage.pop(0)
                storage.append(ord(pixValue))

                sys.stdout.write(pixValue) #write to output
                i += 1
            byte_count += 1
            pixValue = image.read(1)


#Variable to go along with input
storeRetrieve = argStoreRetrieve
if(argHiddenFile != ''):
    hiddenFile = argHiddenFile

#Choose to either store or receive message. Call correct function depending on what is chosen.
if (storeRetrieve == '-s'):
    store(argMethod, int(argOffset), int(argInterval), argWrapperFile, argHiddenFile)
elif (argStoreRetrieve == '-r'):
    retrieve(argMethod, int(argOffset), int(argInterval), argWrapperFile);

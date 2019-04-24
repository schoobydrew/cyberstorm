import socket
import sys
from time import time
from operator import itemgetter
from binascii import unhexlify

##### CONSTANTS #####

# if SETUP is true, the program will find the
# appropriate time delay between characters
# in order to receive the correct output
SETUP = True

# IP address of the server you want to connect to
ip = '138.47.102.201'
# Port at that IP address
port = 33333
# delay of time gap that denotes a '0' binary bit
ZERO = 0.1 # seconds
# delay of time gap that denotes a '1' binary bit
ONE = 0.06 # seconds
# what decimal place to round the timing of delays
ROUND = 3
errorRange = .6
##### PROGRAM FUNCTIONS #####

# function that receives the data and measures the
# time delay between receiving each character and then
# maps each delay into a dictionary
def map_delays(s):
    # create a dictionary to store all delays
    delays = {}
    # create an array to store the delays in order
    # so that different settings can be tested
    delay_array = []
    # time the delay of each character received and
    # increment that key in the dictionary
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    delta = round(t1 - t0, ROUND)
    # first entry into the dictionary so it gets
    # a value of 1
    delays[delta] = 1
    # add delta to the array
    delay_array.append(delta)
    sys.stdout.write(data)
    sys.stdout.flush()
    while (data.rstrip("\n") != "EOF"):
        t0 = time()
        data = s.recv(4096)
        t1 = time()
        delta = round(t1 - t0, ROUND)
        delay_array.append(delta)
        if (delta in delays):
            delays[delta] += 1
        else:
            delays[delta] = 1
        sys.stdout.write(data)
        sys.stdout.flush()
    s.close()
    print "\nDELAY    :   FREQUENCY"
    binFreq = 0
    zeroMODE = []
    for k, v in sorted(delays.items(), key=itemgetter(1), reverse=True):
        if (binFreq < 2):
            #assumes that ONE will be larger than ZERO, but frequency of ONES and ZEROES is unknown
            #the mode of 1 will be in either the first or second iteration
            zeroMODE.append(k)
            binFreq += 1
        print ("%f   :   %d" % (k, v))
    #update ONE to be the highest occuring greatest delay*.9 to give an error range
    ONE = max(zeroMODE)*errorRange
    print "setting ONE to: {}".format(ONE)
    print "If wrong set ONE to {}".format(min(zeroMODE)*errorRange)
    delay_array.pop(0)
    print convert(delta_to_binary(delay_array))

def delta_to_binary(deltas):
    covert_bin = ""
    for delta in deltas:
        if (delta >= ONE):
            covert_bin += "1"
        else:
            covert_bin += "0"
    return covert_bin

# function that receives the data and measures the
# time delay between receiving each character and
# converts the respective delays into binary
def receive(s):
    delay_array = []
    data = s.recv(4096)
    sys.stdout.write(data)
    sys.stdout.flush()
    while (data.rstrip("\n") != "EOF"):
        t0 = time()
        data = s.recv(4096)
        t1 = time()
        delta = round(t1 - t0, ROUND)
        delay_array.append(delta)
        sys.stdout.write(data)
        sys.stdout.flush()
    s.close()
    print
    return delta_to_binary(delay_array)


# function that takes a binary string as an input
# and converts it to an ASCII string
def convert(binary):
    message = ""
    i = 0
    while (i < len(binary)):
        # process one byte at a time
        b = binary[i:i + 8]
        n = int("0b{}".format(b), 2)
        try:
            message += unhexlify("{0:x}".format(n))
            #message += chr(int(b, 2))
        except TypeError:
            message += "?"
        # stop at the string "EOF"
        if(message[:-3] == "EOF"):
            break
        i += 8
    return message

##### MAIN #####
if __name__ == "__main__":
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    s.connect((ip, port))
    if (SETUP):
        print "Gathering Delays..."
        print ""
        map_delays(s)
    else:
        print convert(receive(s))

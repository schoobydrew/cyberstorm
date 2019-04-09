import time
import socket
from binascii import hexlify

##### CONSTANTS #####

# time delay to denote a binary '0' (seconds)
ZERO = 0.025
# time delay to denote a binary '1' (seconds)
ONE = 0.1
# port you want to send a message through
PORT = 1338
# overt message you want to send
MESSAGE = "This is the overt message that you want to send."
# covert message you want to send
COVERT = "Covert"


# function that takes in a string message
# and converts it to binary
def convert(message):
    covert = COVERT + "EOF"
    binary = ""
    for i in covert:
    # this will add the hex representation of the ascii character
        binary += bin(int(hexlify(i), 16))[2:].zfill(8)
    return binary

# function that sends your message to the client
# while introducing delays between characters
# to convey a covert message
def send(c, addr, message):
    # convert the covert message you want to send into binary
    binary = convert(COVERT)
    n = 0
    print "Sending message..."
    for i in message:
        c.send(i)
        if (binary[n] == '0'):
            time.sleep(ZERO)
        else:
            time.sleep(ONE)
        n += 1
    # send "EOF" to signify the end of the transmission
    c.send("EOF")
    print "Message sent, closing connection."
    c.close()

# function that starts the server and gets ready
# to send the message to the client
def start():
    print "Starting server..."
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to all interfaces on some port
    s.bind(("", PORT))
    # listen for connections
    s.listen(0)
    print "Listening for a connection..."
    # accept a connecting client
    c, addr = s.accept()
    print "Connection successful..."
    return c, addr
    
##### MAIN #####
if __name__ == "__main__":
    c, addr = start()
    # send the message
    send(c, addr, MESSAGE)

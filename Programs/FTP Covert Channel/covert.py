# By Team Persia
# FTP Covert Channel Decoder
# github: github.com/schoobydrew/cyberstorm


import ftplib

###### Global variable for FTP server ######

# FTP server address
ftp_addr = 'jeangourd.com'
# FTP server usernam
ftp_user = 'anonymous'
# FTP directory to change into upon logging in
ftp_dir = "10"
# method of decoding either 10-bit or 7-bit
METHOD = 10


# decode method is given an array of strings containing the binary
# representation for each character in the message
def decode(message):
    # initialize an output string
    # convert each chunk of binary into asscii and append it to the output
    output = ""
    for binary in message:
        output += chr(int(binary, 2))
    return output


# getCovert method is given an array of file listings in the 
# specified directory
def getCovert(listing):
    # initialize a string to hold the file permissions
    permissions = ""
    # take the first 10 charcters of each entry and append
    # it to the permissions string
    for item in listing:
        permissions += item[:10]
    # convert permissions to binary
    binary = ""
    for bit in permissions:
        if (bit == '-'):
            binary += '0'
        else:
            binary += '1'
    # if 7-bit decoding is enabled, exclude all 10-bit chunks
    # that have any of the first 3 bits enabled
    if (METHOD == 7):
        # store 10-bit chunks into an array
        chunks = []
        i = 0
        while (i < len(binary)):
            chunks.append(binary[i:i+10])
            i += 10
        # check each chunk to see if any of the first bits are
        # 1, if none are, append to the newbinary array/list
        newbinary = []
        for chunk in chunks:
            if (chunk[0] != '1' and chunk[1] != '1' and chunk[2] !='1'):
                newbinary.append(chunk)
  

    # if 10-bit decoding is enabled use all bits and split into 7-bit chunks
    # and if length of binary is not divisible by 7 pad it with 0's until it is
    elif (METHOD == 10):
        if (len(binary) % 7 != 0):
            for i in range(0, len(binary) % 7):
                binary += '0'
        # store 7-bit chunks into an array
        newbinary = []
        i = 0
        while (i < len(binary)):
            newbinary.append(binary[i:i+7])
            i += 7
    
    # return the resulting newbinary array/list that holds each
    # binary representation of the ascii characters in the message
    return newbinary

def ftp():
    # initialize the output string
    s = ""
    # create an FTP object
    ftp = ftplib.FTP(ftp_addr)
    # login
    ftp.login(user=ftp_user)
    # chang to appropriate directory
    if (ftp_dir != ""):
        ftp.cwd(ftp_dir)
    # initialize a list to store file listings
    listing = []
    # fetch directory listing and append each entry
    ftp.dir(listing.append)
    # parse through the list to get covert message binary
    m = getCovert(listing)
    # decode the binary message
    s = decode(m)
    return s


#### Main ####
if __name__ == "__main__":
    s = ""
    s = ftp()
    print s

#by Team Persia
#FTP Covert Channel Decoder
#github: github.com/schoobydrew/cyberstorm
#
#
#
#global address and directory
#ftp address
ftp_address = "jeangourd.com"
#ftp user
ftp_user = "anonymous"
#directory
#ftp directory
ftp_directory = ""
#
#
#
from ftplib import FTP
#binary decoder to ascii
#parameters: message as string, bit length integer
#returns: ascii string
def decode(message,bitlength=8):
    return ''.join(chr(int(message[i*bitlength:i*bitlength+bitlength],2)) for i in range(len(message)//bitlength))
#binary decoder launcher
#parameters: message in binary as string
#returns: string from decode function, sometimes will present two versions in the case the binary message length is divisible by both 7 and 8
def bin_to_ascii(message):
    s = ""
    if (len(message)%7 == 0):
        s += decode(message,7) + "\n"
    if (len(message)%8 == 0):
        s += decode(message) + "\n"
    return s
#parses through the given directory listing and returns the covert string
#parameters: array of strings of directory listing
#returns: binary covert message as string
def getCovert():
    return covert
#main function, launches ftp connection and gets directory
#parameters: none, takes in global variables at top
#returns: finished ascii string 
def ftp():
    s = ""
    ftp = FTP(ftp_address)
    ftp.login(user=ftp_user)
    if (ftp_directory != ""):
        ftp.cwd(ftp_directory)
    listing = []
    ftp.dir(listing.append)
    m = getCovert(listing)
    s = bin_to_ascii(m)
    return s
if __name__ == "__main__":
    s = ""
    s = ftp()
    print s

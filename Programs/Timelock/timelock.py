#Team Persians
#Timelock
#github.com/schoobydrew/cyberstorm
from hashlib import md5
import datetime
import sys
import time
#global for manual time entering
currentTime = "2017 03 23 18 02 06"
def getTime():
    if (currentTime != ""):
        time = currentTime.split(" ")
        time = [int(x) for x in time]
        time = datetime.datetime(time[0],time[1],time[2],time[3],time[4],time[5])
    else:
        time = datetime.datetime.now()
    return time
def getEpoch():
    time = raw_input()
    time = time.split(" ")
    time = [int(x) for x in time]
    time = datetime.datetime(time[0],time[1],time[2],time[3],time[4],time[5])
    return time
def getCode(delta):
    #set number of numbers and letters in the code according to algorithm
    digest = md5(md5(str(delta)).hexdigest()).hexdigest()
    letters = [c for c in digest if c.isalpha()]
    numbers = [c for c in digest if c.isdigit()]
    numbers.reverse()
    code = ""
    codeLet = "".join(letters)
    codeNum = "".join(numbers)
    if (len(codeLet) < 2):
        code += codeLet
        code += codeNum[:(4-len(codeLet))]
    elif (len(codeNum) < 2):
        code += codeLet[:2]
        code += codeNum
        code += codeLet[2:4-len(codeNum)]
    else:
        code += codeLet[:2] + codeNum[:2]
    return code
if (__name__ == "__main__"):
    epoch = getEpoch()
    currTime = getTime()
    delta = (currTime-epoch).total_seconds()
    delta = int(((delta//60)*60)-3600)
    print getCode(delta)

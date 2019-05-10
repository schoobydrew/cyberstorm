from pynput.keyboard import Key, Listener
from time import time
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

def on_press(key):
	global keysPress,pressTime
	try:
		pressTime.append(time())
		keysPress.append(key)
	except AttributeError:
		print str(key)

def on_release(key):
	global keysRelease,releaseTime
	releaseTime.append(time())
	keysRelease.append(key)
	if (key == Key.esc):
		return False

keysPress=[]
pressTime=[]
keysRelease=[]
releaseTime=[]

with Listener(on_press = on_press, on_release = on_release) as listener:
	listener.join()

string=""

keysPress = keysPress[:-1]
keysRelease = keysRelease[:-1]

for keys in keysPress:
	string +=str(keys)[2] + ","

for i in range(len(keysPress)-1):
	string += str(keysPress[i])[2] + str(keysPress[i+1])[2] + ","

string = string[:-1] + "\n"

i=0
while True:
	if keysPress[i] == keysRelease[i]:
		string += str(releaseTime[i] - pressTime[i]) + ","
	else:
		for j in range(len(keysPress)-1):
			if (keysPress[i] == keysRelease[j] and j>i):
				string += str(releaseTime[j] - pressTime[i]) + ","
	i += 1
	if i == len(keysPress):
		break

for i in range(len(keysPress)-2):
	string += str(pressTime[i+1] - pressTime[i]) + ","

string = string[:-1]

print string

tcflush(stdout,TCIFLUSH)

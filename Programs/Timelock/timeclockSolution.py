# Team Persian
# Timeclock
# Note: Please install the 'pytz' module before running this program
# Python version - 2.7.12
# github: https://github.com/schoobydrew/cyberstorm/blob/master/Programs/Timelock/timeclockSolution.py

import hashlib
from datetime import datetime
import pytz
import select
import sys

# Use HARDCODE variable to manually set current time
HARDCODE = True
current_time = "2010 06 13 12 55 34"

# Function to split the string to list
def split_string_to_int(time):
  time = time.split()
  time = [int(data) for data in time]
  return time

# Function to get timestamp
def get_utc_timestamp(date_time):
  date_time = split_string_to_int(date_time)
  dt = datetime(date_time[0], date_time[1], date_time[2], date_time[3], date_time[4], date_time[5])
  timestamp = (dt - datetime(1970, 1, 1)).total_seconds()
  return timestamp

# Function to check for daylight saving
def is_summer_time(time):
  time = split_string_to_int(time)
  naive = datetime(time[0], time[1], time[2], time[3], time[4], time[5])
  pacific = pytz.timezone('US/Central')
  aware = pacific.localize(naive, is_dst=None) 
  return bool(aware.dst())

# Function to get hash
def get_hash(elapsed_time):
  first_hash = hashlib.md5(str(elapsed_time).encode('utf-8')).hexdigest()
  second_hash = hashlib.md5(first_hash.encode('utf-8')).hexdigest()
  alphabets = [char for char in second_hash if char.isalpha()]
  digits = [char for char in second_hash if char.isdigit()]
  digits.reverse()
  return alphabets[0]+alphabets[1]+digits[0]+digits[1]

if __name__ == "__main__":
  # check of input
  if select.select([sys.stdin,],[],[],0.0)[0]:
    epoch_time = sys.stdin.read().lstrip().rstrip()
    # get current system time
    if HARDCODE == False:
      current_time = datetime.now().strftime("%Y %m %d %H %M %S")
    current_timestamp = get_utc_timestamp(current_time)
    epoch_timestamp = get_utc_timestamp(epoch_time)
    current_time_check = is_summer_time(current_time)
    epoch_time_check = is_summer_time(epoch_time)
    # calculate time elapsed
    elapsed_time = int(current_timestamp - epoch_timestamp)
    # Check if times are different
    if(current_time_check != epoch_time_check):
      elapsed_time -= 3600
    if elapsed_time % 60 != 0:
      elapsed_time = (elapsed_time/60)*60
    # Calculate and print the code
    md5_hash = get_hash(elapsed_time)
    print(md5_hash)
    print("Current system time: "+ datetime.now().strftime("%Y %m %d %H %M %S"))
  else:
    print("usage:")
    print("python timeclockSolution.py < {filename}")
    print("echo '{Date}' | python timeclockSolution.py")
    print("<install 'pytz' before running this program>")  

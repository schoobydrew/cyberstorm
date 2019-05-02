#!/bin/bash

method="B"                        # B for Byte || b for Bit
action="r"                        # r for Retrieve || s for Store
offset=1024                       # 1024 is what we have commonly used
intervalFormula="2**x"            # keep the x at the end
upperIntervalBound=$((2**8))      
wrapper="stegged-byte.bmp"  
hidden=""                         # only needed for storage

if [ $action == 'r' ] ; then
    x=0
    interval=0
    while [[ $interval -lt $upperIntervalBound ]] ; do
        interval=$((${intervalFormula: :-1}$x))
        python steg.py -$method -$action -o$offset -i$interval -w$wrapper > temp$interval
        x=$(($x+1))
    done

elif [ $action == 's' ] ; then
    python steg.py -$method -$action -o$offset -i$interval -w$wrapper -h$hidden > new
fi

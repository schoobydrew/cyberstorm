#!/bin/bash

method="B"                        # B for Byte || b for Bit
offset="2**x"
offsetUpperBound=$((2**8))                       # 1024 is what we have commonly used
intervalFormula="2**x"            # keep the x at the end
upperIntervalBound=$((2**8))      
wrapper="0c947c0c57d1407bd6e2d7f1092bb057.bmp"  

x=0
y=0
interval=0
offset=0
while [[ $offset -lt $upperIntervalBound ]] ; do
    while [[ $interval -lt $upperIntervalBound ]] ; do
        interval=$((${intervalFormula: :-1}$x))
        python steg.py -$method -$action -o$offset -i$interval -w$wrapper > temp$interval
        x=$(($x+1))
    done
    y=$(($y+1))
done

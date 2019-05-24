#!/bin/bash

method="B"

offsetStart=1024
offsetFormula="2**x"
offsetEnd=$((2**16))

intervalStart=1
intervalFormula="2**x"
intervalEnd=$((2**6))

wrapper="stegged-byte.bmp"

o=0
offset=$offsetStart

while [[ $offset -lt $offsetEnd ]]; do
    offsetAdd=0
    if [ $o -ne "0" ]; then
        offsetAdd=$((${offsetFormula: :-1}$o))
        offset=$(($offset*$offsetAdd))
    fi
    i=0
    interval=$intervalStart
    while [[ $interval -lt $intervalEnd ]]; do
        intervalAdd=$((${intervalFormula: :-1}$i))
        interval=$((interval+$intervalAdd))
        python steg.py -$method -r -o$offset -i$interval -w$wrapper > $PWD/Dump/temp"$offset"_"$interval"
        
        i=$(($i+1))
    done
    o=$((o+1))
done

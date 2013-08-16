#!/bin/bash  
i=0 
while [ $i -lt 20 ]  
do  
    ((i++))  
    echo -ne "=>\033[s"  
    echo -ne "\033[40;50H"$((i*5*100/100))%"\033[u\033[1D"  
    sleep 0.3  
done  
echo 

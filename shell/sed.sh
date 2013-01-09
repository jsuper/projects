#!/bin/bash
if [ $# != 1 ]
then
    echo "Usage: sed.sh inputfile"
else
    for line in $(sed -n '/licenselabel/=' $1)
    do 
	y=$line
	declare -i y
	let "y+=1" 
	cmd="$y"p
        sed -n "$cmd" $1 | sed "/.*\<.*--.*/p"
#	echo "abcd" | sed "s/bc/ef/g"
    done
fi

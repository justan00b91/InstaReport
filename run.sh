#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage: $0 <Insta User Name>"
	exit 1
else
	echo "Checking for $1"
	instaloader $1
	sleep 10
	if [ -d $1 ]; then
		cp main.py $1
	        cd $1
        	python3 main.py
		rm -rf main.py
	        xdg-open index.html
		echo "Done"
	fi
	echo "Error downloading for $1"
	echo "Exitting ..."
	exit 0
fi

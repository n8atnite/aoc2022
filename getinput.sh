#!/bin/bash

if [ ! $1 ]; then
    echo -e "Please provide a day as a single integer.\nUsage: ./getinput.sh [DAY]"
    exit 1
fi

if [ ! -f cookie.txt ]; then
    echo "You must log in to adventofcode.com first and save your session cookie. See the README for details."
    exit 2
fi 

if [ ! -d days/$1 ]; then
    mkdir -p days/$1
fi

AOC_COOKIE=$(< cookie.txt)
YEAR=2022
curl --cookie "$AOC_COOKIE" https://adventofcode.com/$YEAR/day/$1/input > ./days/$1/input$1.txt
touch days/$1/sol1.py
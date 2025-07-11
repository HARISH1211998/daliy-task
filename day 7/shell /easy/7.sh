## Task Shell Script – Easy
## ✅ Task: Write a shell script that: Accepts a filename as input, Prints the number of lines that contain a specific word (ask the user for the word too), Hint: Use grep -c

#!/bin/bash

read -p "Enter the file: " file

if [ ! -f "$file" ]; then
    echo "Given input is not a file format"
    exit 1
fi
read -p "Enter the word to search: " word
count=$(grep -c "$word" "$file")
echo "The word '$word' appears in $count line(s) in the file."

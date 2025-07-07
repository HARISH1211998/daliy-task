# Task Task:
# Write a script that accepts a filename and prints:
# Whether it exists
# Whether it’s a file or directory
# Its size in human-readable format

#!/bin/bash

read -p "Get file from: " file

if [ ! -e "$file" ]; then
    echo "Give the file is not exists"
fi

size=$(du -sh "$file" | cut -f1)
if [ -f "$file" ]; then
    echo "Given file is on file formet: $size"
elif [ -d "$file" ]; then
    echo "Given files is an directory: $size"
else 
    echo "it is not file or directory"
fi




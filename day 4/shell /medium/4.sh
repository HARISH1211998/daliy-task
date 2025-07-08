## Write a shell script that: Accepts a directory path, Lists all files modified in the last 7 days
#! /bin/bash

read -p "Enter the directory path: " dir

if [ ! -d "$dir" ]; then
    echo "The path is not a directory."
    exit 1
fi

echo "Files modified in the last 7 days in '$dir':"
find "$dir" -type f -mtime -7
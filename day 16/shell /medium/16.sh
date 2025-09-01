## Shell – Medium
## Task: Accept a directory path and calculate total size of .txt files.

#!/bin/bash

read -p "Enter the directory path: " dir

if [[ ! -d "$dir" ]]; then
    echo "Given path is not a directory"
    exit 1
fi

# Calculate total size of .txt files in human-readable format
total_size=$(find "$dir" -type f -name "*.txt" -exec du -ch {} + | grep total$ | awk '{print $1}')

echo "Total size of .txt files in $dir: $total_size"
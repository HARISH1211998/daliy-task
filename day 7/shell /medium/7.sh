## Task Task:
# Write a shell script that: Accepts a directory path, Lists the top 5 largest .log files, including subdirectories,Print their name and size, Hint: Use find, du, sort, head
#!/bin/bash

read -p "Enter the directory: " dir

if [ ! -d "$dir" ]; then
    echo "Given path is not directory"
    exit 1
fi

find "$dir" -type f -name "*.log" -exec du -h {} + 2>/dev/null | sort -hr | head -n 5
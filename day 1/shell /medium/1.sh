# Day 1 – Medium Level Tasks 🔸 Bash Script (Medium) Task: Write a shell script to monitor 
# disk usage and print a warning if any mounted disk is more than 80% full. (Hint: Use df, awk, and conditionals.)
#! /bin/bash

echo "Checking disk usage..."

THRESHOLD=80

# Loop through each line of 'df -h' excluding header
df -h | grep '^/dev/' | while read line; do
    usage=$(echo $line | awk '{print $5}' | tr -d '%')
    mount_point=$(echo $line | awk '{print $1}')

    if [ "$usage" -gt "$THRESHOLD" ]; then
        echo "Warning: Disk usage on $mount_point is ${usage}%"
    fi
done

## Task: Accept a directory path. Recursively find:
## All .log files larger than 1MB, Print their path and size, Hint: Use find, -size +1M, -name "*.log"
 
#!/bin/bash

read -p "Enter the directory: " dir

if [ ! -d "$dir" ]; then
    echo "Given input is not a directory"
    exit 1
fi

# Print total and used memory in MB
read total used <<< $(free -m | awk '/^Mem:/ {print $2, $3}')

echo "Memory usage:"
echo "Total Memory: ${total}MB"
echo "Used Memory:  ${used}MB"

# Find all .log files larger than 1MB
echo "Log files larger than 1MB in $dir:"
find "$dir" -type f -name "*.log" -size +1M -exec ls -lh {} \; | awk '{print $9, $5}'
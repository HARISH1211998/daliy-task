## Task Task: Monitor memory usage and alert if usage crosses 80% (Hint: Use free, awk, or vm_stat if on Mac)
## Print "Memory usage high: XX%" if over 80%.

#!/bin/bash

# Threshold
max=80

# Get memory values from `free` in MB
read total used <<< $(free -m | awk '/^Mem:/ {print $2, $3}')

# Calculate usage percentage
usage_percent=$((100 * used / total))

if [ "$usage_percent" -gt "$max" ]; then
    echo "Memory usage high: ${usage_percent}%"
else
    echo "Memory usage is OK: ${usage_percent}%"
fi

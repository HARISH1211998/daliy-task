# task
# Write a script that:
# Accepts a directory path as input
# Counts how many .log files are in that directory
# Shows the total size of those .log files combined

#!/bin/bash

read -p "Enter a directory path: " dir

# Fix: convert to absolute path if it's relative
if [[ ! -d "$dir" ]]; then
  echo "❌ Directory does not exist: $dir"
  exit 1
fi

# Count .log files (case-sensitive match)
log_count=$(find "$dir" -type f -name "*.log" | wc -l)

# Get total size of .log files (in human-readable format)
log_size=$(find "$dir" -type f -name "*.log" -exec du -ch {} + 2>/dev/null | grep total$ | awk '{print $1}')

echo "✅ Number of .log files: $log_count"
echo "📦 Total size of .log files: $log_size"


# Task:
# Write a script to find the top 3 largest files in a directory (including subdirectories).
# (Hint: Use find, du, sort, head)

read -p "Enter the directory: " dir

if [ ! -d "$dir" ]; then
    echo "Given path is not an directory"
    exit 1
fi

find "$dir" -type f -exec du -h {} + 2>/dev/null | sort -hr | head -n 2
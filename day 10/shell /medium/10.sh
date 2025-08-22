### Day 10 shell script Task: Accept a directory path and count the total number of subdirectories inside it
#!/bin/zsh

read -p "Enter the directory to get subdirectory: " dir

if [[ ! -d "$dir" ]]; then
    echo "Given path is not Directory"
fi

# Count subdirectories (excluding the parent itself)
count=$(find "$dir" -mindepth 1 -type d | wc -l)

echo "Total number of subdirectories inside '$dir': $count"


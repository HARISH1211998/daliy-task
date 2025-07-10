## Task Medium – Shell Script
## Task: Write a shell script to: Accept a directory from the user, Count how many files are older than 7 days
# Show their names and sizes, 📌 Hint: Use find, -mtime, -type f, -exec ls -lh

read -p "Enter the directory from to check the file:" dir

if [ ! -d "$dir" ]; then
    echo "Give input is not an directory"
fi

find "$dir" -type f -mtime +7 -exec ls -lh {} \; | awk '{print $9, $5}'
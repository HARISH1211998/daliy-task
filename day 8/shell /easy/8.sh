## Task: Accept a file name and print the total number of blank lines in it.
# (Hint: grep, awk, or sed)

read -p "Get the file and find out the space: " file

if [ ! -f "$file" ]; then
    echo "Give input is not an file"
    exit 1
fi

grep -c '^[[:space:]]*$' "$file"
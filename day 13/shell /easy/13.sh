## Shell – Easy
## Task: Accept a filename and print the first 5 lines. (Hint: head -5)

read -p "Enter the filename: " file

if [[ ! -f "$file" ]]; then
    echo "Given input is not an file"
    exit 1
fi

head -n 5 "$file"
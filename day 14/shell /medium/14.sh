## Shell – Medium
## Task: Accept a filename and count how many unique words it contains.

read -p "Enter the sentence: " file

if [[ ! -f "$file" ]]; then
    echo "Given the file is not path"
fi 

# Count unique words
tr -s '[:space:]' '\n' < "$file" | tr -d '[:punct:]' | sort -u | wc -l
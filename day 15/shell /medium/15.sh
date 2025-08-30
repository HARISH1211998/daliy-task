read -p "Enter the file: " file

if [[ ! -f "$file" ]]; then
    echo "File not found: $file"
    exit 1
fi

sort "$file"
## Task Plan ✅ Easy – Shell Script
# Task: Write a shell script to: Accept a filename from the user, Print only the lines that are not empty
# 📌 Hint: Use grep or awk (Bonus: ignore lines that have only spaces)

read -p "Enter the file name: " file

# Check if file exists
if [ ! -f "$file" ]; then
    echo "File not found!"
    exit 1
fi

echo "Non-empty lines in $file:"
grep -v '^[[:space:]]*$' "$file"

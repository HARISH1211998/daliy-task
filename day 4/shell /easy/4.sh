# Task Write a shell script that:
# Accepts a filename as input
# Prints how many lines, words, and characters are in the file

read -p "Enter the file path: " file

# Check if file exists
if [ ! -f "$file" ]; then
    echo "❌ Given value is not a valid file."
    exit 1
fi

# Count lines, words, and characters
line_count=$(wc -l < "$file")
word_count=$(wc -w < "$file")
char_count=$(wc -c < "$file")

# Print results
echo "📄 File Analysis:"
echo "👉 Number of lines      : $line_count"
echo "👉 Number of words      : $word_count"
echo "👉 Number of characters : $char_count"
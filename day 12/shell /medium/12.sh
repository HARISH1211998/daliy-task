## 🐚 Shell – Medium
## Task: Accept a filename and replace all spaces with underscores. (Hint: tr or sed)

read -p "Enter the file to change the replace all space in _" file

if [[ ! -e "$file" ]]:
    echo "Enter into the file"
fi

# Replace spaces with underscores and save into a new file
sed 's/ /_/g' "$file" > "${file}_modified"

echo "Updated file saved as ${file}_modified"
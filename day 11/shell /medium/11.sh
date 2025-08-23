## Shell – Medium
## Task: Accept a directory path and archive it into a .tar.gz file.

# Archive name will be directory_name.tar.gz
archive_name="$(basename "$dir").tar.gz"

tar -czvf "$archive_name" -C "$(dirname "$dir")" "$(basename "$dir")"

echo "Archive created: $archive_name"

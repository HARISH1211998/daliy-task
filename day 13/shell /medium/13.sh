## Shell – Medium
## Task: Accept a directory path and find all symbolic links inside it.

read -p "Accept a directory path:" dir

if [[ ! -d "$dir" ]];then
    echo "Given path is not directory"
fi

echo "Symbolic links inside $dir:"
find "$dir" -type l
### Day 10 shell script Task: Accept a filename and print the last 10 lines. (Hint: use tail)

read -p "Enter the file name to print last 10line: " file

if [[ ! -f "$file" ]]; then
    echo "Give the input is not an file"
fi
 
echo "---- First 10 lines ----"
head -n 10 "$file"

echo "---- Last 10 lines ----"
tail -n 10 "$file"
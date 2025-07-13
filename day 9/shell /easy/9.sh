## Task: Accept a file name and print only the lines that start with a capital letter.
## Hint: Use grep, ^[A-Z]

#!/bin/bash

#!/bin/bash

read -p "Enter the file name: " file

if [ ! -f "$file" ]; then
    echo "Given input is not a file"
    exit 1
fi

# Correct pattern: lines starting with a capital letter
grep '^[A-Z]' "$file"
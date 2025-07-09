## Task: Write a shell script to: Accept a number from the user, Check if the number is even or odd, 📌 Hint: Use modulo % operator in Bash.
#!/bin/bash
read -p "Enter the value to check the odd or even: " num

if [[ "$num" =~ ^[0-9]+$ ]]; then
    echo "Give number is valid integer"
else
    echo "Give input is not integer"
    exit 1
fi

if (($num % 2 == 0)); then
    echo "Give number is even"
else
    echo "Give number is odd"
fi
# Write a shell script to check if a given number is even or odd.
#!/bin/bash

echo "Give me the number to verify odd or even:"
read number

if (( number % 2 == 0 )); then
    echo "Given number is even"
else
    echo "Given number is odd"
fi

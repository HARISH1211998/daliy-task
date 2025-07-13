# daliy-task
Day 1 – Easy Level Tasks
🔹 Bash Script (Easy)
Task:
Write a shell script to check if a given number is even or odd.
Ask the user for input and print the result.

🔹 Python Script (Easy)
Task:
Write a Python program that takes a sentence from the user and prints how many words it contains.

🧠 Day 1 – Medium Level Tasks
🔸 Bash Script (Medium)
Task:
Write a shell script to monitor disk usage and print a warning if any mounted disk is more than 80% full.
(Hint: Use df, awk, and conditionals.)

🔸 Python Script (Medium)
Task:
Write a Python program that accepts a string from the user and checks whether it is a palindrome (ignore spaces, punctuation, and case).
Example: "A man a plan a canal Panama" → Palindrome ✅


## Day 2 task 6th july
✅ Easy-Level Tasks
🔹 Python (Easy)
Task:
Write a program to accept a list of numbers from the user (space-separated), and print the sum of all the numbers.

🔹 Shell Script (Easy)
Task:
Write a shell script that prints the current date, time, logged-in user, and hostname.

🧠 Medium-Level Tasks
🔸 Python (Medium)
Task:
Write a Python program that reads a string and prints all unique characters (characters that appear only once).
For example: input → "engineering" → output → ['g', 'r']

🔸 Shell Script (Medium)
Task:
Write a script that:
Accepts a directory path as input
Counts how many .log files are in that directory
Shows the total size of those .log files combined


## Day 3 task 7th july
✅ Easy-Level Tasks
🔹 Shell Script (Easy)
Task:
Write a script that accepts a filename and prints:
Whether it exists
Whether it’s a file or directory
Its size in human-readable format

🔹 Python (Easy)
Task:
Write a program to accept a string and print each word on a new line.
For example: "Hello World from Python" →
Hello  
World  
from  

🔸 Shell Script (Medium)
Task:
Write a script to find the top 3 largest files in a directory (including subdirectories).
(Hint: Use find, du, sort, head)

🔸 Python (Medium)
Task:
Write a Python program that accepts a list of integers and returns all the duplicate numbers in the list.
Example:
Input:  [1, 2, 3, 4, 2, 5, 1, 6]
Output: [1, 2]


## Day 4 task 8th july
Easy – Shell Script
Task:
Write a shell script that:
Accepts a filename as input
Prints how many lines, words, and characters are in the file
📌 (Hint: Use wc command)

✅ Easy – Python
Task:
Write a Python program that:
Accepts a string
Counts the number of vowels (a, e, i, o, u) in it

🧠 Medium – Shell Script
Task:
Write a shell script that:
Accepts a directory path
Lists all files modified in the last 7 days
📌 (Hint: Use find with -mtime)

🧠 Medium – Python
Task:
Write a Python program to:
Accept a string from the user
Return the first non-repeating character
Example: input "programming" → output 'p'

## Day 5
✅ Day 5 Task Plan
✅ Easy – Shell Script
Task:
Write a shell script to:
Accept a number from the user
Check if the number is even or odd
📌 Hint: Use modulo % operator in Bash.

✅ Easy – Python
Task:
Write a Python program to:
Accept a number from the user
Print the multiplication table up to 10
📌 Example:
Input → 5
Output → 5 x 1 = 5, ..., 5 x 10 = 50

🧠 Medium – Shell Script
Task:
Write a shell script to:
Monitor a given process by name (e.g., nginx, python)
If the process is not running, print a message
📌 Hint: Use pgrep or ps -ef | grep to check the process.

🧠 Medium – Python
Task:
Write a Python program to:Accept a sentence
Count how many times each word appears
📌 Example:
Input → "this is a test this is only a test"
Output →
this: 2  
is: 2  
a: 2  
test: 2  
only: 1



Day 6 Task Plan
✅ Easy – Shell Script
Task:
Write a shell script to:
Accept a filename from the user
Print only the lines that are not empty
📌 Hint: Use grep or awk
(Bonus: ignore lines that have only spaces)

✅ Easy – Python
Task:
Write a Python program to:
Accept a number from the user
Print whether it is a prime number or not
📌 Example:
Input: 7 → Output: "7 is a prime number"
Input: 10 → Output: "10 is not a prime number"

🧠 Medium – Shell Script
Task:
Write a shell script to:
Accept a directory from the user
Count how many files are older than 7 days
Show their names and sizes
📌 Hint: Use find, -mtime, -type f, -exec ls -lh

🧠 Medium – Python
Task:
Write a Python program to:
Accept a sentence from the user
Find and print the longest word in the sentence
Example:
Input: "DevOps makes deployment easier"
Output: "deployment" is the longest word


## Day 7 
🐍 Python – Easy
✅ Task:
Write a Python program to accept a string from the user and print the number of uppercase and lowercase letters in it.
📌 Example:
Input: Hello World
Output:
Uppercase letters: 2  
Lowercase letters: 8

🐚 Shell Script – Easy
✅ Task:
Write a shell script that:
Accepts a filename as input
Prints the number of lines that contain a specific word (ask the user for the word too)
Hint: Use grep -c

🐍 Python – Medium
✅ Task:
Write a Python program that:
Accepts a list of integers from the user (comma-separated)
Finds the second largest unique number
📌 Example:
Input: 10, 20, 20, 30, 10
Output: 20

🐚 Shell Script – Medium
✅ Task:
Write a shell script that:
Accepts a directory path
Lists the top 5 largest .log files, including subdirectories
Print their name and size
Hint: Use find, du, sort, head


## Day 8
🐍 Python – Easy
Task: Accept a string from the user and print all the digits found in it.
Example:
Input → abc123xyz9
Output → Digits: 1, 2, 3, 9

🐚 Shell – Easy
Task: Accept a file name and print the total number of blank lines in it.
(Hint: grep, awk, or sed)

🐍 Python – Medium
Task: Accept a sentence, and return the word with the highest number of vowels.
Example:
Input → Automation makes life easier
Output → Automation

🐚 Shell – Medium
Task: Monitor memory usage and alert if usage crosses 80%
(Hint: Use free, awk, or vm_stat if on Mac)
Print "Memory usage high: XX%" if over 80%.



## Day 9
Python – Easy
✅ Task: Accept a list of comma-separated strings and print only the strings with length > 5.
Example:
Input → apple,banana,dog,elephant
Output → banana, elephant


🐚 Shell – Easy
✅ Task: Accept a file name and print only the lines that start with a capital letter.
Hint: Use grep, ^[A-Z]

🐍 Python – Medium
✅ Task: Accept a sentence from the user and print:
All words longer than the average word length

Example:
Input → "DevOps makes deployments easier and faster"
Average word length → 6
Output → deployments, easier

🐚 Shell – Medium
✅ Task: Accept a directory path. Recursively find:
All .log files larger than 1MB
Print their path and size
Hint: Use find, -size +1M, -name "*.log"
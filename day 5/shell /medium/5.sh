## Task Medium – Shell Script
# Task: Write a shell script to: Monitor a given process by name (e.g., nginx, python), If the process is not running, print a message
# 📌 Hint: Use pgrep or ps -ef | grep to check the process.

read -p "Enter the process checking: " process

if pgrep "$process" > cat /dev/null
then
    echo "The process is running"
else
    echo "the process is not running"
fi
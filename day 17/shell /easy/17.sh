## Shell – Easy
## Task: Accept a process ID (PID) and print its status. (Hint: ps -p PID)
#!/bin/bash

read -p "Enter the process ID: " PID

# Check if PID is a number
if ! [[ "$PID" =~ ^[0-9]+$ ]]; then
    echo "Error: PID must be a number."
    exit 1
fi

# Check if process exists and print status
if ps -p "$PID" > /dev/null 2>&1; then
    echo "Process status:"
    ps -p "$PID" -o pid,ppid,cmd,stat
else
    echo "No process found with PID $PID"
fi


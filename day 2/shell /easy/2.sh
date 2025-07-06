## Task 
# Write a shell script that prints the current date, time, logged-in user, and hostname.
#!/bin/bash

echo "Current date and time: $(date)"
echo "Logged-in user: $(whoami)"
echo "Hostname: $(hostname)"

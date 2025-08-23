## Shell – Easy
## Task: Display the current disk usage in human-readable format. (Hint: df -h)
 
df -h . | awk 'NR==2 {print "MEM: " $3, "Capacity: " $5}'
## 🐍 Python – Easy
## Task: Task: Display the top 5 CPU-consuming processes. (Hint: ps aux --sort=-%cpu | head -n 6)
echo "Top 5 CPU consuming processes:"
ps aux --sort=-%cpu | head -n 6
## Shell – Medium
## Task: Monitor CPU usage and alert if usage crosses 75%.
#!/bin/bash

# Set CPU threshold (default: 75%)
THRESHOLD=75

while true; do
    # Get the top CPU consuming process (skip header)
    CPU_USAGE=$(ps -eo %cpu --sort=-%cpu | sed -n '2p' | cut -d. -f1)

    if [ "$CPU_USAGE" -gt "$THRESHOLD" ]; then
        echo "⚠️ Alert: CPU usage is at ${CPU_USAGE}% (threshold: ${THRESHOLD}%)"
    else
        echo "CPU usage normal: ${CPU_USAGE}%"
    fi

    # Wait 5 seconds before checking again
    sleep 5
done

# Shell – Easy
# Task: Display the default gateway of your system. (Hint: ip route show or netstat -rn)

#!/bin/bash

ip route show | grep '^default' | awk '{print $3}'
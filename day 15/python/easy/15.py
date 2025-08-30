## Python – Easy
## Task: Accept two numbers and print their greatest common divisor (GCD).

import math

# Accept input
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

# Find GCD
gcd = math.gcd(first, second)

print(f"The Greatest Common Divisor (GCD) of {first} and {second} is: {gcd}")
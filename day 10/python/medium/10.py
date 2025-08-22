### Task day 10 -> Task: Accept a list of numbers and print the median value.(The median is the "middle value" when numbers are sorted in ascending order.
# If the list has odd numbers → the middle element is the median.
# If the list has even numbers → the median is the average of the two middle elements.

# Examples

# Case 1: Odd number of values
# Numbers: 3, 1, 7
# Sorted: 1, 3, 7
# 👉 Middle value = 3 (Median = 3)

# Case 2: Even number of values
# Numbers: 10, 40, 20, 30
# Sorted: 10, 20, 30, 40
# 👉 Middle two values = 20 and 30
# Median = (20 + 30) ÷ 2 = 25 )

import statistics

def main():
    user_input = input("Enter the list of number: ")
    split_input = user_input.split(',')
    # converted into integer
    numbers = [int(num.strip()) for num in split_input]
    # Calculate median
    median_value = statistics.median(numbers)
    print(f"The median is: {median_value}")

if __name__ == "__main__":
    main()
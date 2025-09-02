## Python – Medium
## Task: Implement a simple calculator (add, subtract, multiply, divide).

def main():
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))

    sum_number = number1 + number2
    subtract_number = number1 - number2
    multiply_number = number1 * number2
    
    # Handle division safely
    if number2 != 0:
        divide_number = number1 / number2
    else:
        divide_number = "Undefined (division by zero)"

    print(f"Addition of two numbers: {sum_number}")
    print(f"Subtraction of two numbers: {subtract_number}")
    print(f"Multiplication of two numbers: {multiply_number}")
    print(f"Division of two numbers: {divide_number}")

if __name__ == "__main__":
    main()

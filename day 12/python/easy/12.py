## 🐍 Python – Easy
## Task: Accept a number and print its factorial.
def main():
    user_value = int(input("Enter the input: "))
    factorial = 1
    for i in range(1, user_value + 1):
        factorial *= i
    print(f"Factorial of {user_value} is {factorial}")

if __name__ == "__main__":
    main()
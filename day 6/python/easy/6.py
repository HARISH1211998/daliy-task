# Task: Write a Python program to: Accept a number from the user Print whether it is a prime number or not
# 📌 Example:
# Input: 7 → Output: "7 is a prime number"
# Input: 10 → Output: "10 is not a prime number"

def main():
    value=int(input("Enter the value: "))
    if value <= 1:
        print(f"Give value is not prime number{value}")
    for i in range(2, int(value ** 0.5) + 1):
        print(value)
        print(value ** 0.5, i)
        if value % i == 0:
            print(f"{value} is not a prime number")
            return
    print(f"{value} is a prime number")

if __name__ == "__main__":
    main()
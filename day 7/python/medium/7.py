## Task  Python – Medium
## ✅ Task: Write a Python program that:
## Accepts a list of integers from the user (comma-separated) Finds the second largest unique number
## 📌 Example: Input: 10, 20, 20, 30, 10, Output: 20

def main():
    user_input = input("Enter the numbers (comma-separated): ")
    
    # Step 1: Split and convert to integers
    numbers = [int(num.strip()) for num in user_input.split(",")]
    
    # Step 2: Get unique numbers
    unique_numbers = list(set(numbers))

    # Step 3: Sort the list in descending order
    unique_numbers.sort(reverse=True)
    # Step 4: Pick second largest if available
    if len(unique_numbers) >= 2:
        print(f"Second largest number is: {unique_numbers[1]}")
    else:
        print("There is no second unique number.")

if __name__ == "__main__":
    main()

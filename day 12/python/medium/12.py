## 🐍 Python – Medium
## Task: Accept a list of numbers and remove all even numbers.
def main():
    user_input = input("Enter the user list (comma-separated): ")
    split_input = user_input.split(",")
    numbers = [int(num.strip()) for num in split_input]
    
    number_odd = []
    for number in numbers:
        if number % 2 != 0: 
            number_odd.append(number)

    print("List after removing even numbers:", number_odd)

if __name__ == "__main__":
    main()
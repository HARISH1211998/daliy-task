## Python – Easy
## Task: Accept a list of numbers and print the maximum and minimum numbers.
def main():
    user_input = input("Enter numbers separated by commas: ")
    numbers = [int(num.strip()) for num in user_input.split(",")]
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
if __name__ == "__main__":
    main()
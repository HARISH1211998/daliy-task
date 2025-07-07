# Task: Write a Python program that accepts a list of integers and returns all the duplicate numbers in the list.
def main():
    input_number=input("Enter the list of number: ")
    numbers=input_number.split(',')
    original_num=[int(num.strip()) for num in numbers]
    seen=set()
    duplicate=set()
    for num in original_num:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    print("Duplicate numbers:", list(duplicate))
if __name__ == "__main__":
    main()

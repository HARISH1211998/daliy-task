## 🐍 Python – Easy
## Task: Accept a list of numbers and print only positive numbers.

def main():
    inp_int = input("Enter numbers separated by spaces: ")
    numbers = [int(num) for num in inp_int.split()]

    print("Positive numbers are:")
    for num in numbers:
        if num > 0:
            print(num)

if __name__ == "__main__":
    main()
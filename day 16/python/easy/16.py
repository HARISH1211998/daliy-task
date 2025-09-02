## Python – Easy
## Task: Accept a number and print its binary representation.
def main():
    # Take input from user
    num = int(input("Enter a number: "))
    
    # Convert to binary (removes '0b' prefix with [2:])
    binary_representation = bin(num)[2:]
    
    print(f"Binary representation of {num} is: {binary_representation}")

if __name__ == "__main__":
    main()

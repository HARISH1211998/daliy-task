## Task:
## Write a Python program that: Accepts a string, Counts the number of vowels (a, e, i, o, u) in it
def main():
    user_word = input("Enter the input word: ")
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Using a set for efficient lookup
    count = 0

    for char in user_word.lower():
        if char in vowels:
            count += 1

    print(f"Number of vowels in the word: {count}")

if __name__ == "__main__":
    main()
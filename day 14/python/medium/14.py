## 🐍 Python – Medium
## Task: Accept a sentence and count the frequency of each character.
def main():
    sen = input("Enter the sentence: ")
    frequency = {}

    for char in sen:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    print("Character frequencies:")
    for char, freq in frequency.items():
        print(f"'{char}': {freq}")

if __name__ == "__main__":
    main()
## Task: Write a Python program to accept a string from the user and print the number of uppercase and lowercase letters in it.
# 📌 Example: Input: Hello World, Output: Uppercase letters: 2, Lowercase letters: 8
def main():
    user_input = input("Enter the string: ")
    upper_letters = {}
    lower_letters = {}

    for ch in user_input:
        if ch.islower():
            lower_letters[ch] = lower_letters.get(ch, 0) + 1
        elif ch.isupper():
            upper_letters[ch] = upper_letters.get(ch, 0) + 1

    print(f"Uppercase letters count: {sum(upper_letters.values())}")
    print(f"Lowercase letters count: {sum(lower_letters.values())}")
    print(f"Uppercase breakdown: {upper_letters}")
    print(f"Lowercase breakdown: {lower_letters}")

if __name__ == "__main__":
    main()
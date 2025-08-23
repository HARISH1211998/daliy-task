## Python – Medium
## Task: Accept a string and check if it’s a palindrome.
def main():
    user_input = input("Enter a word or phrase: ")
    # normalize: lowercase + remove spaces
    cleaned_input = user_input.replace(" ", "").lower()
    reverse_input = cleaned_input[::-1]

    if cleaned_input == reverse_input:
        print("The given input is a palindrome ✅")
    else:
        print("The given input is not a palindrome ❌")

if __name__ == "__main__":
    main()

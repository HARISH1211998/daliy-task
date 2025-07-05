def main():
    sentence = input("Enter the sentence to check the palindrome: ")
    lower_case = sentence.lower()
    
    argument_case = []
    for char in lower_case:
        if char.isalnum():
            argument_case.append(char)
    
    cleaned = ''.join(argument_case)
    if cleaned == cleaned[::-1]:
        print("Given sentence or word is a palindrome")
    else:
        print("Not a palindrome")

if __name__ == "__main__":
    main()

## Task: Write a Python program to: Accept a string from the user, Return the first non-repeating character
## Example: input "programming" → output 'p'

def main():
    user_word=input("Enter the string: ")
    char_count={}
    for ch in user_word:
        char_count[ch] = char_count.get(ch, 0) + 1
    print(char_count)
    for ch in user_word:
        if char_count[ch] == 1:
            print(f"First the of word repeated: {ch}")
            return
    print("❌ No non-repeating character found.")
if __name__ == "__main__":
    main()
# Task:Write a Python program to: Accept a sentence from the user Find and print the longest word in the sentence
# Example: Input: "DevOps makes deployment easier" Output: "deployment" is the longest word
def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()  # Splits on any whitespace

    # Use max with key = len to get the longest word
    longest = max(words, key=len)

    print(f"The longest word is: '{longest}' with length {len(longest)}")

if __name__ == "__main__":
    main()
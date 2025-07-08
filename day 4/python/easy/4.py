## Task:
## Write a Python program that: Accepts a string, Counts the number of vowels (a, e, i, o, u) in it
from collections import Counter
def main():
    user_word = input("Enter the input word: ").lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counter = Counter(ch for ch in user_word if ch in vowels)
    print("Vowel counts:", dict(counter))

if __name__ == "__main__":
    main()
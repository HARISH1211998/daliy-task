## Python – Easy
## Task: Accept a string and count how many consonants it has.

def main():
    given_input = input("Enter the string: ").lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set()
    count = 0
    for ch in given_input:
        if ch.isalpha() and ch not in vowels:  # check if letter and not vowel
            count += 1
            consonants.add(ch)
    print(f"Consonant count: {count}")
    print(f"Unique consonants found: {consonants}")

if __name__ == "__main__":
    main()
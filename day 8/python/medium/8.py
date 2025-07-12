## Task: Accept a sentence, and return the word with the highest number of vowels.
## Example: Input → Automation makes life easier, Output → Automation

def main():
    sent=input("Enter the sentence input: ").lower()
    vowels=[ 'a', 'e', 'i', 'o', 'u']
    sentence=sent.split()
    max_vowel_word=""
    max_vowel_count=0
    for se in sentence:
        count = 0
        for word in se:
            if word in vowels:
                count +=1
        if max_vowel_count < count:
            max_vowel_count = count
            max_vowel_word = se

    print(f"Word with highest vowels: {max_vowel_word} ({max_vowel_count} vowels)")

if __name__ == "__main__":
    main()

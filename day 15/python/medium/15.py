## Python – Medium
## Task: Accept a sentence and reverse the order of words.
def main():
    inp_sen = input("Enter the sentence: ")
    words = inp_sen.split()             # split into words
    reversed_words = words[::-1]        # reverse word order
    result = " ".join(reversed_words)   # join back into sentence
    print("Reversed sentence:", result)

if __name__ == "__main__":
    main()
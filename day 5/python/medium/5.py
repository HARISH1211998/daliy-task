## Task: Write a Python program to:Accept a sentence
# Count how many times each word appears
# 📌 Example:
# Input → "this is a test this is only a test"
# Output →
# this: 2  
# is: 2  
# a: 2  
# test: 2  
# only: 1

def main():
    input_sentence=input("Enter the input sentence: ")
    test=input_sentence.split(" ")
    word_pass={}

    for word in test:
        word_pass[word]=word_pass.get(word, 0) + 1
    print(word_pass)
    
    for we, count in word_pass.items():
        print(f"{we}: {count}")

if __name__ == "__main__":
    main()
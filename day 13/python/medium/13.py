## Python – Medium
## Task: Accept a list of words and sort them alphabetically.
def main():
    input_sentence = input("Enter the sentence: ")
    words = input_sentence.split()   
    words.sort()                    
    print("Sorted words:", words)

if __name__ == "__main__":
    main()
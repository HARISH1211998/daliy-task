# Write a Python program that takes a sentence from the user and prints how many words it contains.
def main():
    print("print the sentence with repeated word")
    sentence=input("Enter the sentence:")
    count=sentence.split()
    print("Number of the word in the sentence:", len(count))

if __name__ == "__main__":
    main()
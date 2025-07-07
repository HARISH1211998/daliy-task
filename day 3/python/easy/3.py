# Task: Write a program to accept a string and print each word on a new line.
def main():
    word_list = input("Enter the list of words: \n")
    words = word_list.split()  # Splits on whitespace by default
    for word in words:
        print(word)

if __name__ == "__main__":
    main()

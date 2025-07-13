## Task: Accept a list of comma-separated strings and print only the strings with length > 5.
## Example: Input → apple,banana,dog,elephant, Output → banana, elephant

def main():
    leng=input("Enter the string value: ")
    word=leng.split(",")
    for wo in word:
        if len(wo) > 5:
            print(wo)

if __name__ == "__main__":
    main()
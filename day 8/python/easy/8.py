## Task: Accept a string from the user and print all the digits found in it.
## Example: Input → abc123xyz9, Output → Digits: 1, 2, 3, 9

def main():
    st=input("Enter the input value: ")
    integers=[]
    for str in st:
        if str.isdigit():
            integers.append(str)
    print("Digits:", ", ".join(integers))
if __name__=="__main__":
    main()
# task
# Write a Python program that reads a string and prints all unique characters (characters that appear only once).
# For example: input → "engineering" → output → ['g', 'r']
def main():
    user_value=input("Enter the input value(unique string): ")
    unique_chars=[]
    for str in user_value:
        if user_value.count(str) == 1:
            unique_chars.append(str)
    print(unique_chars)

if __name__ == "__main__":
    main()
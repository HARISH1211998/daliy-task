##  Task:
# Write a Python program to: Accept a number from the user Print the multiplication table up to 10
# 📌 Example:
# Input → 5
# Output → 5 x 1 = 5, ..., 5 x 10 = 50
def main():
    user_input=int(input("Enter the integer: "))
    for x in range(1,11):
        print(f"{user_input} * {x} = {user_input * x}")

if __name__ == "__main__":
    main()
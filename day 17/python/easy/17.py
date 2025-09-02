# Python – Easy
# Task: Accept a list of numbers and print only odd numbers.
def main():
    input_list = input("Enter the input list: ")
    split_input = input_list.split(",")
    number_list = [int(num.strip()) for num in split_input]

    odd_numbers = []  
    for number in number_list:
        if number % 2 != 0:   
            odd_numbers.append(number)
    print("Odd numbers:", odd_numbers)

if __name__ == "__main__":
    main()
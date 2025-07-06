## task 
# Write a program to accept a list of numbers from the user (space-separated), and print the sum of all the numbers.


def main():
    user_number=input("get the list of the number: ")
    number_list=user_number.split()

    int_num=[]
    for num in number_list:
        int_num.append(int(num))
    total=sum(int_num)
    print(total)

if __name__ == "__main__":
    main()
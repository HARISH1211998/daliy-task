### Task day 10 -> Task: Accept a string and count how many spaces are in it.
def main():
    user_str = input("Enter the String to find out the space: ")
    space_count = user_str.count(" ")

    if space_count > 0: 
        print(f"The string contains {space_count} spaces.")   
    else:
        print(f"Give input didn't have spaces.") 

if __name__ == "__main__":
    main()
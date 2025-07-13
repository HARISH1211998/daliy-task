## Task Accept a sentence from the user and print: All words longer than the average word length

def main():
   lon=input("Enter the longest word: ")
   sen=lon.split()
   total_length = 0
   for word in sen:
      total_length += len(word)
   average = total_length / len(sen)
   print(f"Average value of the sentence: {average}")
       
if __name__ == "__main__":
    main()
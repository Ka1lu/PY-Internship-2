def wordscount(text):
    #Counts the number of words in a given text.
    if not text.strip():
        return 0
    return len(text.split())

while True:
    try:
        entry = input("Enter the given sentence or paragraph: ").strip()

        if not entry:
            print("Error: Input cannot be empty. Please enter valid text.")
            continue

        total_words = wordscount(entry)
        print(f"The total words in the input are: {total_words}")

        breakstatus = input('''\nPress 1 to exit\nPress any other key to run again\n''')
        if breakstatus == '1':
            print("Exiting the program. Thank you!")
            break

    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")



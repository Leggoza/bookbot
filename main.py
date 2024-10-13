# Import os to work with file paths
import os

def count_characters(text):
    lowercase_text = text.lower() # Convert text to lowercase
    character_count = {}
    
    for character in lowercase_text:
        if character.isalpha(): # Only proceed if the character is an alphabet letter
            if character in character_count:
                character_count[character] = character_count[character] + 1
            else:
                character_count[character] = 1

    return character_count

def main():
    file_path = "books/frankenstein.txt"

    with open("books/frankenstein.txt") as f:
        book = f.read()
    
    # Count the number of words
    word_list = book.split() # Split the text into individual words
    word_count = len(word_list) # Get the length of the list to count the number of words

    result = count_characters(book)

    # Extract the filename from the path
    file_name = os.path.basename(file_path)

    # Printing the report heading, including the filename
    print(f"---Beginning report of {file_name}---\n")

    # Printing the word count
    print(f"A total of {word_count} words were found in this document.\n")


    # Loop through each character and count in the dictionary
    for character, count in result.items():
        # Use an f-string to create a unique message every line
        print(f"The '{character}' character was found {count} times")

    print("\n---End of report---")

if __name__ == "__main__":
    main()
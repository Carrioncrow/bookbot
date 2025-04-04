import sys
from stats import get_character_count, get_num_words, sorted_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1] #relative path from your main.py file
    text = get_book_text(path)
    word_count = get_num_words(text)
    char_count = get_character_count(text)
    sorted_chars = sorted_dict(char_count)  # Changed variable name to avoid conflict
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Now iterate through sorted characters and print them
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

# Call the main function
main()
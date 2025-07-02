import sys
from stats import get_num_words
from stats import get_sorted_characters



if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
else:
    character_count = get_sorted_characters()
    word_count = get_num_words()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---------- Character Count -------")
    for character, count in character_count.items():
        if character.isalpha():  # Only print alphabetic characters
            print(f"{character}: {count}")
    print("============= END ===============")

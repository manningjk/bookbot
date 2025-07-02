import sys
# Function that returns the number of words in a book
# The function reads the book, splits it into words, and returns the count of words
def get_num_words():
    with open(sys.argv[1], 'r') as f:
        file_contents = f.read()
        words = str.split(file_contents)
        num_words =  len(words)
        return num_words

# Function that returns a dictionary with the count of each character in a book
# The function reads the book, converts it to lowercase, and counts the occurrences of each lette
def get_num_characters():
    with open(sys.argv[1], 'r') as f:
        file_contents = f.read()
        make_lower = str.lower(file_contents)
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        character_count_dict = {}
        for letters in make_lower:
            if letters in character_count_dict:
                character_count_dict[letters] += 1
            else:
                character_count_dict[letters] = 1
        
        return character_count_dict
    
# Function that returns a sorted dictionary with the count of each character in a book
# The function reads the book, converts it to lowercase, and counts the occurrences of each letter
def get_sorted_characters():
    character_count_dict = get_num_characters()
    sorted_character_count = dict(sorted(character_count_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_character_count
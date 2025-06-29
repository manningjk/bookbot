def get_num_words():
        with open("./books/frankenstein.txt", encoding="utf-8") as f:
                file_contents = f.read()
                words = str.split(file_contents)
                num_words =  len(words)
        print(f"{num_words} words found in the document")

get_num_words()


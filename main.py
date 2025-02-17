# Read contents of books

def main(path_to_file):
    text_file = read_file(path_to_file)
    #word_count = count_words(text_file)
    #print(word_count)

    result = count_characters(text_file)
    print(result)

def read_file(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
        
    return file_contents

def count_words(text):
    return len(text.split())

def count_characters(text):
    #ignore case
    char_count = {}
    for c in text.lower():
        count = 0
        if c in char_count:
            count = char_count[c]
        count = count + 1
        char_count[c] = count

    return char_count

main("./books/frankenstein.txt")
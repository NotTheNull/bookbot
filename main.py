# Read contents of books

def main(path_to_file):
    text_file = read_file(path_to_file)
    word_count = count_words(text_file)
    print(word_count)

def read_file(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
        
    return file_contents

def count_words(text):
    #words = text.split()
    return len(text.split())

main("./books/frankenstein.txt")
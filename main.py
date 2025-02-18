# Read contents of books

def main(path_to_file):
    text_file = read_file(path_to_file)
    word_count = count_words(text_file)
    result = count_characters(text_file)
    list_counts = convert_and_sort(result)
    report = build_report(path_to_file, word_count, list_counts)
    print(report)


def build_report(path_to_file, word_count, char_counts):
    report = f"--- Begin report of {path_to_file} ---\n"
    report += f"{word_count} words found in the document\n"

    #NOTE: we only want the alphabet characters
    for c in char_counts:
        if c["char"] < 'a': continue
        if c["char"] > 'z': continue
        report += f"\nThe '{c["char"]}' character was found {c["count"]} times"

    report += "\n--- End report ---"
    return report

def convert_and_sort(dict_chars):
    list_chars = []
    
    for c in dict_chars:
        json = {"char": c, "count": dict_chars[c]}
        list_chars.append(json)

    list_chars.sort(reverse=True, key=sort_char_count)
    return list_chars

def sort_char_count(dict):
    return dict["count"]


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
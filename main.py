from stats import number_of_words, number_of_chars, char_list_of_dicts, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    num_words = number_of_words(text)
    print(f"Found {num_words} total words")
    num_chars = number_of_chars(text)
    print("--------- Character Count -------")
    char_list = char_list_of_dicts(num_chars)
    char_list.sort(reverse=True, key=sort_on)

    for i in range(0, len(char_list)):
        if char_list[i]["char"].isalpha():
            print(f"{char_list[i]["char"]}: {char_list[i]["num"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()

#books/frankenstein.txt
import sys
from stats import get_num_words, get_chars, sort_on, chars_to_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def report(book, total, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    file_content = get_book_text(book)
    total = get_num_words(file_content)
#    print(f"Found {total} total words")
    char_counts = get_chars(file_content)
#    for k, v in char_counts.items():
#        print(f"'{k}': {v}")

    sorted_list = chars_to_sorted(char_counts)
    report(book, total, sorted_list)

#    print(char_counts)
main()

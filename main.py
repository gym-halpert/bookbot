from stats import get_num_words, get_chars, sort_on, chars_to_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def report(filepath, total, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def main():
    filepath = "books/frankenstein.txt"
    file_content = get_book_text("books/frankenstein.txt")
    total = get_num_words(file_content)
#    print(f"Found {total} total words")
    char_counts = get_chars(file_content)
#    for k, v in char_counts.items():
#        print(f"'{k}': {v}")

    sorted_list = chars_to_sorted(char_counts)
    report(filepath, total, sorted_list)

#    print(char_counts)
main()

from stats import count_words, char_counts, sort_on, dictionary_sort

def get_book_text(filepath):
    filepath = "../books/frankenstein.txt"
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "../books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = count_words(text)
#    print(f"Found {total_words} total words")
    char_dictionary = char_counts(text)
    sorted_dictionary = dictionary_sort(char_dictionary)
#    print(char_dictionary)
#    print(dictionary_sort(char_dictionary))
    report(book_path, total_words, sorted_dictionary)

def report(book_path, total_words, sorted_dictionary):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dictionary:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

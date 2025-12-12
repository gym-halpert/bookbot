from stats import get_num_words, get_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    file_content = get_book_text("books/frankenstein.txt")
    total = get_num_words(file_content)
    print(f"Found {total} total words")
    char_counts = get_chars(file_content)
    for k, v in char_counts.items():
        print(f"'{k}': {v}")

main()

from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    file_content = get_book_text("books/frankenstein.txt")
    total = get_num_words(file_content)
    print(f"Found {total} total words")
main()

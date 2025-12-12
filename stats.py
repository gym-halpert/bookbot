def get_num_words(file_content):
    total = 0
    for i in file_content.split():
        total += 1
    return total

def get_chars(file_content):
    char_counts = {}
    for word in file_content.split():
        for char in word:
            ch = char.lower()
            if ch not in char_counts:
                char_counts[ch] = 1
            else:
                char_counts[ch] += 1
    return char_counts

def sort_on(dictionary):
    return dictionary["num"]

def chars_to_sorted(char_counts):
    sorted = []
    for i in char_counts:
        sorted.append({"char": i, "num": char_counts[i]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

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

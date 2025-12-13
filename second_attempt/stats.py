def count_words(text):
    words = 0
    for word in text.split():
        words += 1
    return words

def char_counts(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1
    return chars

def sort_on(dictionary):
    return dictionary["num"]

def dictionary_sort(char_dictionary):
    sorted = []
    for char in char_dictionary:
        sorted.append({"char": char, "num": char_dictionary[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

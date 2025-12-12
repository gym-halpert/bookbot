def get_num_words(file_content):
    total = 0
    for i in file_content.split():
        total += 1
    return total

def split_into_words(lines):
    words = []
    for line in lines:
        words.extend(words.strip(",.!?") for words in line.split())
    return words

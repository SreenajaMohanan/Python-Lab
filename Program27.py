def longestWord(word)
    max_length = len(word[0]
    for item in word:
        length = len(item)
        if length > max_length:

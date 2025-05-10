def swap(word):
    word = list(word)
    for i in range(1, len(word), 2):
        word[i-1],word[i] = word[i],word[i-1]
    return "".join(word)
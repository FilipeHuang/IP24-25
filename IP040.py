def remove_all(word, ch):
    a = ""
    for i in word:
        if i != ch:
            a += i
    return a
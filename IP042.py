def count(word, letters): 
    a = 0
    for i in word: 
        if i in letters: a += 1
    return a
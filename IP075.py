def word_types(lst):
    a, b, c = 0, 0, 0
    for i in lst:
        if i.islower(): a += 1
        elif i.isupper(): b += 1
        else: c += 1
    return (a, b, c)
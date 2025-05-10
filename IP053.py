def occurrences(lst, x):
    a =[]
    if lst.count(x) == 1: a.append(lst.index(x))
    elif lst.count(x) != 1:
        for i in range(len(lst)):
            if lst[i] == x: a.append(i)
    return a
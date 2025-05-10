def eeny_meeny(lst, k):
    a = []
    i = 0
    while lst:
        i = (i + k - 1) % len(lst)
        a.append(lst.pop(i))
    return a
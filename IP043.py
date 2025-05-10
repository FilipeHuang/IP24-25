def search(tup, value):
    if value not in tup: return (-1, -1)
    for i in range(len(tup)):
        if tup[i] == value: 
            a1 = i
            break
    for j in range(len(tup)-1, -1, -1):
        if tup[j] == value: 
            a2 = j
            break
    return (a1, a2)
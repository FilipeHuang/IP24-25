def duplicate(tup):
    a = ()
    for i in tup:
        a += (i,i)
    return a
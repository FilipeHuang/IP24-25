def sum(a,b):
    c = []
    for i in range(len(a)):
        k = []
        for j in range(len(a[i])):
            k.append(a[i][j]+b[i][j])
        c.append(k)
    return c
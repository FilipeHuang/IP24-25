def pascal(n):
    a = [1]
    if n == 1: pass
    else:
        for i in range(1, n):
            b = [1]
            for j in range(1, i):
                b.append(a[j-1]+a[j])
            b.append(1)
            a = b
    return a
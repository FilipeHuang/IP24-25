def fibonacci(a, b, n):
    lst = [a]
    while len(lst)<n:
        lst.append(b)
        a,b = b, a+b
    return lst
def sum_all_odds(a, b):
    c = 0
    c1 = min(a, b)
    c2 = max(a, b)
    for i in range(c1, c2+1):
        if i%2!=0:
            c += i
    return c
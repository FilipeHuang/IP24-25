def whichone(n):
    if n == 1:
        return "A"
    l1, l2 = 1, 1
    while n > l2:
        l1, l2 = l2, l1 + l2
    while n > 2:
        if n > l1:
            n -= l1
        l1, l2 = l2 - l1, l1
    return "A" if n == 1 else "B"
print(whichone(4))
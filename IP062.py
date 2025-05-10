def spiral_number(y,x):
    if x > y:
        if x % 2 == 1:
            a = x ** 2 - (y - 1)
        else:
            a = x ** 2 - (2 * x - y -1)
    elif y > x:
        if y % 2 == 0:
            a = y ** 2 - (x - 1)
        else:
            a = y ** 2 - (2 * y - x -1)
    else:
        a = y ** 2 - x + 1
    return a
def transform(lst):
    t1 = []
    for i in lst:
        t2 = []
        for j in i:
            try:
                n = int(j)
                t2.append(1/n)
            except ZeroDivisionError: print(f'Error: ZeroDivisionError for value "{j}": division by zero.')
            except ValueError : print('Error: ValueError for value',f'"{j}": invalid literal for int() with base 10:',f"'{j}'.")
        if t2: t1.append(t2)
    return t1
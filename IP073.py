def possible(digits, a, b):
    k = 0
    for i in range(a,b+1):
        i_str = str(i)
        prop = 1
        for j in i_str:
            if j not in digits:
                prop = 0
                break
        if prop:
            k += 1
    return k
def largest_sequence(num):
    l = 1
    l_max = 1
    for i in range(len(str(num))-1):
        if str(num)[i] < str(num)[i+1]:
            l += 1
        else:
            l_max = max(l, l_max)
            l = 1
    l_max = max(l, l_max)
    return l_max
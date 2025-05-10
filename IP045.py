def substring(needle, haystack):
    count = 0
    for i in haystack:
        if i == needle[count]: count += 1
        if count == len(needle): return True
    return False
def find_all(keyword, text):
    lst = []
    i = 0
    while True:
        a = text.find(keyword, i)
        if a == -1: break
        lst.append(a)
        i = a + 1
    return lst
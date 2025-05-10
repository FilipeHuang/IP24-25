def remove(x, menu):
    a = set()
    for i in menu:
        if x not in i[0]: a.add(i)
    menu.clear()
    menu.update(a)

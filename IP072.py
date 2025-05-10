def super_swap(menu):
    new = {}
    for k,v in menu.items():
        if v not in new: new[v] = set()
        new[v].add(k)
    return new
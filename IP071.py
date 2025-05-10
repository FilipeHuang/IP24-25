def frequency(ingredients):
    dict = {}
    a = set(ingredients)
    for i in a:
        n = ingredients.count(i)
        dict[i] = n
    return dict
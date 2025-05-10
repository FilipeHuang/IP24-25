def sort_strings(lst):
    lst.sort(key = lambda x:(-len(x),x))
    return lst
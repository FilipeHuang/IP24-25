def middle(lst):
    a = []
    lst.sort()
    if len(lst)%2==0: a.extend([lst[len(lst)//2-1],lst[len(lst)//2]])
    else: a.append(lst[len(lst)//2])
    return a
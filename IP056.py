def list_to_matrix(lst, r, c):
    a = []
    for i in range(0,len(lst),c):
        a.append(lst[i:i+c])
    return a
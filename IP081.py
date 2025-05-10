def sort_initials(text):
    a = {}
    for i in text.split():
        c = i[0].lower()
        if c in a: a[c]+=1
        else: a[c]=1
    #elements of lst are in a tuple of 2 elements
    lst =[(k,v) for k,v in a.items()]
    #reverse the order by the number of the second element
    #then order it again with the 1st (the letter)
    lst.sort(key = lambda x : (-x[1],x[0]))
    return "".join(k[0] for k in lst)
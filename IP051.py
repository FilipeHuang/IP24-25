def rotate(lst,dir):
    if not lst:
        return lst
    if dir == "right": 
        lst.insert(0,lst.pop())
    elif dir == "left": 
        lst.append(lst.pop(0))
    return lst
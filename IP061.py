def rmv_lst(m):
        while [] in m:
            m.remove([])
def spiral_path(m):
    a = []
    while len(m) > 0:
        a.extend(m.pop(0))
        rmv_lst(m)
        if len(m) == 0: break
        for i in range(len(m)):
            if m[i]: a.append(m[i].pop())
        rmv_lst(m)
        if len(m) == 0: break
        a.extend(m[-1][::-1])
        m.pop()
        rmv_lst(m)
        if len == 0: break
        for j in range(len(m)-1,-1,-1):
            if m[j]: a.append(m[j].pop(0))
        rmv_lst(m)
    return a
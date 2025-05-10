def read():
    global r,k,l
    r,k = map(int,input().split())
    l = input()
def bit8(r):
    bi = []
    while r > 0:
        bi.append(r%2)
        r //= 2
    while len(bi) < 8: bi.append(0)
    reversed(bi)
    return bi
def s2n(trip):
    n = 0
    if trip[0] == "#": n += 4
    if trip[1] == "#": n += 2
    if trip[2] == "#": n += 1
    return n
def calc(r8,trip):
    return "#" if r8[s2n(trip)] ==1 else "."
def create(r8,l):
    new = []
    l = "." + l + "."
    for i in range(len(l)-2):
        new.append(calc(r8,l[i:i+3]))
    return "".join(new)
def sim():
    global l
    r8 = bit8(r)
    for _ in range(k):
        l = create(r8,l)
        print(l)
read()
sim()
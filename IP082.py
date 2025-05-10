def lenn(a):
    return "+" + a*"-"
def show_table(k, lst):
    r = len(lst)%k
    if r != 0: lst.extend(" "*(k-r))
    table = ""
    a = max([len(i) for i in lst])
    table += lenn(a)*k + "+\n|"
    for i in range(len(lst)):
        n = a-len(lst[i])
        table += " "*n+lst[i]+"|"
        if (i+1)%k==0: 
            table += "\n" + lenn(a)*k + "+"
            if i+1 != len(lst): table += "\n|"
    print(table)
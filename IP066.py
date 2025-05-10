def compose(f,g):
    a = {}
    for i in f:
        if f[i] in g:
            a[i]=g[f[i]]
    return a
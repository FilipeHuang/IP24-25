def future_exceptions(f, a, b):
    n = 0
    for i in range(a,b+1):
        try: f(i)
        except Exception: n += 1
    return n
def csv_change(text, a, b):
    x = text.split(",")
    x[a-1],x[b-1] = x[b-1],x[a-1]
    return ",".join(x)
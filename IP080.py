def extract_numbers(text):
    n = []
    a = ""
    for i in text:
        if i.isdigit(): a += i
        else:
            if a:
                n.append(int(a))
                a = ""
    if a:
        n.append(int(a))
    return n
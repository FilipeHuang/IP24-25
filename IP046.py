def evolve(initial, n):
    print(initial)
    for i in range(n):
        next = ""
        for j in initial:
            if j == "A": next += "AB"
            elif j == "B": next += "A"
        print(next)
        initial = next
evolve("A", 13)
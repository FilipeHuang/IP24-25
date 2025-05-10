def perm(x):
    if len(x) == 1: return [x]
    result = []
    for j in range(len(x)):
        head = x[j]
        rest = x[:j] + x[j+1:]
        for k in perm(rest): result.append([head]+k)
    return result
def visit(planets):
    lst = []
    if len(planets) <= 1: return [planets+planets]
    for i in range(len(planets)):
        planets.insert(0,planets.pop(i))
        for l in perm(planets[1:]): lst.append([planets[0]] + l + [planets[0]])
    return lst
print(sorted(visit(["a"])))
print(sorted(visit(["b","a"])))

# print()

# output = visit(["c","a","b"]) 
# print("output is of type", type(output))
# print("output has size:", len(output))
# for x in sorted(output): print(x)

# print()

# output = visit(["1","2","3","4"]) 
# print("output is of type", type(output))
# print("output has size:", len(output))
# for x in sorted(output): print(x)


# print()

# output = visit(["e","d","c","a","b"]) 
# print("output is of type", type(output))
# print("output has size:", len(output))
# for x in sorted(output): print(x)

# print()

# output = visit(["f","a","c","d","e","b"]) 
# print("output is of type", type(output))
# print("output has size:", len(output))
# for x in sorted(output): print(x)

# print()

# output = visit(["a","b","c","d","e", "f", "g"]) 
# print("output is of type", type(output))
# print("output has size:", len(output))
# for x in sorted(output): print(x)
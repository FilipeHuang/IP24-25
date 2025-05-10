def numbers(k, n, d):
    if k == 1:
        if n == 1: return [d]
        elif n == 0: return [i for i in range(1,10) if i != d]
        return []
    lst = []
    for j in range(10):
        for l in numbers(k-1, n if j != d else n-1, d):
            if l != 0: lst.append(j + l *10)
    return lst
output = numbers(2,1,3)
print(sorted(output))

print()

output = numbers(3,2,5)
print("output is of type", type(output))
print("output has size:", len(output))
for x in sorted(output): print(x)
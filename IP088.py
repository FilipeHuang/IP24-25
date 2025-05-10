def summ(a):
    b = []
    for i in range(len(a)):
        b.append(sum(a[i]))
    return b
def rec(coins,lst):
    if len(coins) == 0: return [lst]
    x = rec(coins[1:],lst + [coins[0]])
    y = rec(coins[1:], lst)
    return x+y
def quantities(coins):
    return set(summ(rec(coins,[])))

output = quantities([10, 50, 100])
print(sorted(output))

print()

output = quantities([1, 1, 5, 5, 12])
print("output is of type", type(output))
print("output has size:", len(output))
for x in sorted(output): print(x)
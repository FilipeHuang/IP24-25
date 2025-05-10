n = int(input())
total = 0
for i in range(1, n+1):
    price = 50/i
    print(f"Night {i}: {round(price,2)}E")
    total += price
print(f"Total: {round(total,2)}E")
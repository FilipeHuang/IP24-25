num = int(input())
order = []
a, d, n= False, False, False
option = ["The number is not ordered.",
        "The number is in ascending order.",
        "The number is in descending order."]
for i in str(num):
    order.append(int(i))
for j in range(len(order)-1):
    if order[j] < order[j+1]:
        a = True
    elif order[j] > order[j+1]:
        d = True
    else:
        n = True
if n or (a and d):
    k = 0
elif a:
    k = 1
else:
    k = 2
print(option[k])
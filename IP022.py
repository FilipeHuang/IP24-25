num = int(input())
list = []
for i in range(num-1,0,-1):
    if num % i == 0: list.append(i)
if sum(list) == num: 
    print(f"{num} is a perfect number")
    for j in list:
        if j == list[0]: print(f"Factors: {j}", end=' ')
        elif j == list[len(list)-1]: print(j)
        else: print(j, end = " ")
else: print(f"{num} is not a perfect number")
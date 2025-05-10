n = int(input())
for i in range(n, 101, n):
    if i == 100 or i+n>100:
        print(i, end = "\n")
    else:    
        print(i, end = " ")
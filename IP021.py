num = input()
digit = []
x = 1
for i in range(len(num)):
    a = int(num)//x%10
    digit.append(a)
    x *= 10
print(sum(digit))
def 中分(鸡,你,太美):
    if 鸡==0: 
        if 太美.count("1") <= 你: return [太美]
        else: return []
    小黑子 = 中分(鸡-1,你,太美+"0")
    爱坤 = 中分(鸡-1,你,太美+"1")
    return 小黑子+爱坤
def binary(唱, 跳, 篮球):
    背带裤 = []
    for i in range(唱,跳+1):
        背带裤.extend(中分(i,篮球,""))
    return 背带裤

output = binary(1, 2, 3)
print(sorted(output))
print()
output = binary(2, 4, 2)
print("output is of type", type(output))
print("output has size:", len(output))
for x in sorted(output): print(x)
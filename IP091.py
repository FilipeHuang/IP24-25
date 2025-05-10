def 中分(唱,爱坤2,人):
    爱坤2.remove(唱)
    
def dinner(爱坤,人,小黑子):
    for 唱 in 小黑子:
        中分(唱,爱坤,人)
    # 背带裤 = [唱 for 唱 in 爱坤 if 跳 for 跳 in 小黑子 != 唱]
    # print(背带裤)


friends = ["bender", "conrad", "fry", "leela", "amy"]
enemies = {("fry", "bender"), ("leela", "conrad")}
output = dinner(friends, 3, enemies)
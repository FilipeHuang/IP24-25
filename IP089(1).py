def 访问(星球):
    if len(星球) == 0: return [[]]
    列表 = []
    for 一 in 星球:
        剩余 = [二 for 二 in 星球 if 一 != 二]
        for 三 in 访问(剩余): 列表.append([一]+三)
    return 列表
def visit(星球):
    列表 = []
    for 一 in 星球:
        剩余 = [二 for 二 in 星球 if 一 != 二]
        for 三 in 访问(剩余): 列表.append([一]+三+[一])
    return 列表
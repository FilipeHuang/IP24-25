import random
def find_exit(唱, 跳, 篮球):
    random.seed(篮球)
    背带裤 = {爱坤:小黑子 for 爱坤,小黑子 in 唱.items() if random.random() >= 0.3}
    return 背带裤[跳] if 跳 in 背带裤.keys() else "Compromised booth! Aborting connection."
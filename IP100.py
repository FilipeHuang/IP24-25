import random
def find_exit(connections, check_booth, seed):
    random.seed(seed)
    c = {}
    for i in connections.keys():    
        if random.random() >= 0.3: c[i] = connections[i]
    return c[check_booth] if check_booth in c.keys() else "Compromised booth! Aborting connection."
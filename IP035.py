import math
def digits_average(n):
    while n >= 10:
        n1 = n % 10
        n //= 10
        alg = 1
        new_n = 0
        while n > 0:
            n2 = n % 10
            avg = math.ceil((n1 + n2)/2)
            new_n += avg * alg
            alg *= 10
            n1 = n2
            n //= 10
        n = new_n
    return n
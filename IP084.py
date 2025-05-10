def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        a,b=b,a+b
    return b
def loop(n):
    i = 0
    while True:
        k = fibonacci(i)
        if k > n:
            x = fibonacci(i - 1)
            break
        i += 1
    return x
def count_range(a,b):
    return loop(b)-loop(a)
print(count_range(3,10))
print(count_range(2,19))
print(count_range(42,297))
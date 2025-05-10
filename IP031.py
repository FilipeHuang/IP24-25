def factorial(x):
    a = 1
    for i in range(2, x+1):
        a *= i
    return a
def combination(n, k):
    if k > n:
        return "NA"
    return int(factorial(n)/(factorial(k)*factorial(n-k)))
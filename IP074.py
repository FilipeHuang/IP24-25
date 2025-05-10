def minimum_coins(coins, k):
    min = 0
    lst = list(coins)
    prop = 1
    for i in lst:
        res = minimum_coins(coins, k - i)
        if res:
            if not prop or res + 1 < 
    return min if k == 0 else -1
print(minimum_coins({1,5,7}, 11))
print(minimum_coins({1,5,10}, 10))
print(minimum_coins({3,6}, 10))
print(minimum_coins({1}, 42))
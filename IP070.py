def possible_sums(coins):
    sums = set()
    l_coins = list(coins)
    for i in range(len(l_coins)):
        sums.add(l_coins[i])
        for j in range(len(l_coins)):
            sums.add(l_coins[i]+l_coins[j])
            for k in range(len(l_coins)):
                sums.add(l_coins[i]+l_coins[j]+l_coins[k])
    return sums
def minimum_coins_strict(n):
    num_coins = 0
    for coin in [25, 10, 5, 1]:
        while n >= coin:
            n -= coin
            num_coins += 1
    return num_coins

n = 16
assert minimum_coins_strict(n) == 3

def minimum_coins_general(n, coins):
    cached = {0 : 0}

    def mcg_dp(amount):
        if amount not in cached:
            smallest = min([mcg_dp(amount - value) for value in coins if amount >= value])
            cached[amount] = smallest + 1
        return cached[amount]

    return mcg_dp(n)

n = 16
coins = [1, 5, 10, 25]
assert minimum_coins_general(n, coins) == 3
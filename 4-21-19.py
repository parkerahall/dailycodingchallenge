def k_buys_and_sells(prices, k):
    cache = {}

    prices_len = len(prices)
    for i in range(k):
        cache[(prices_len - 1, i)] = 0
        cache[(prices_len, i)] = 0

    for j in range(prices_len):
        cache[(j, 0)] = 0

    max_after = {}
    biggest_ind = -1
    for m in range(prices_len - 1, -1, -1):
        if prices[m] >= prices[biggest_ind]:
            biggest_ind = m
            max_after[m] = None
        else:
            max_after[m] = biggest_ind

    def kbas_dp(i, n):
        if (i, n) not in cache:
            max_profit = 0
            for buy in range(i, prices_len - 1):
                sell = max_after[buy]
                if sell != None:
                    profit = prices[sell] - prices[buy]
                    max_profit = max(max_profit, kbas_dp(sell + 1, n - 1) + profit)
            cache[(i, n)] = max_profit

        return cache[(i, n)]

    return kbas_dp(0, k)

prices = [5, 2, 4, 0, 1]
k = 2
assert k_buys_and_sells(prices, k) == 3
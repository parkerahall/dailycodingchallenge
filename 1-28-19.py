def max_profit(prices):
    lowest = float("inf")
    highest = 0
    profit = 0
    for price in prices:
        # if a new minimum price if found, reset highest so only prices after are considered for selling
        if price < lowest:
            lowest = price
            highest = price

        highest = max(highest, price)
        profit = max(profit, highest - lowest)

    return profit

prices = [9, 11, 8, 5, 7, 10]
assert max_profit(prices) == 5
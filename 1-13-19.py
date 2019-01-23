import math

# Basically a boneless Bellman-Ford
def has_negative_cycle(distance):
    num_rows = len(distance)
    num_cols = len(distance[0])

    true_distances = [float("inf")] * num_rows
    true_distances[0] = 1

    for _ in range(num_rows - 1):
        for i in range(num_rows):
            for j in range(num_cols):
                true_distances[j] = min(true_distances[j], true_distances[i] + distance[i][j])

    for i in range(num_rows):
        for j in range(num_cols):
            if true_distances[j] > true_distances[i] + distance[i][j]:
                return True
    return False


def arbitrage(exchange_table):
    assert len(exchange_table) > 0
    assert len(exchange_table[0]) > 0

    num_rows = len(exchange_table)
    num_cols = len(exchange_table[0])

    # exchange_table should be square (exchange rate for every pair of currencies)
    assert num_rows == num_cols

    distance = []
    for i in range(num_rows):
        new_row = []
        for j in range(num_rows):
            new_row.append(-math.log(exchange_table[i][j]))
        distance.append(new_row)

    return has_negative_cycle(distance)



exchange_table = [[1, .5, 1], [1, 1, .5], [4.1, 1, 1]]
assert arbitrage(exchange_table) == True

exchange_table = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
assert arbitrage(exchange_table) == False

exchange_table = [[1, .9, .5], [.2, 1, .8], [.95, .35, 1]]
assert arbitrage(exchange_table) == False
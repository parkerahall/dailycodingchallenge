def minimum_cost(grid):
    assert len(grid) > 0
    assert len(grid[0]) > 0

    last_row = len(grid) - 1
    cached = {(last_row, i) : grid[last_row][i] for i in range(len(grid[last_row]))}
    
    def minimum_cost_dp(grid, n, k):
        if (n, k) not in cached:
            result = grid[n][k] + min([minimum_cost_dp(grid, n + 1, i) for i in range(len(grid[n + 1])) if i != k])
            cached[(n, k)] = result
        return cached[(n, k)]

    return min(minimum_cost_dp(grid, 0, i) for i in range(len(grid[0])))

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert minimum_cost(grid) == 13

grid = [[1, 2, 3], [5, 4, 6], [7, 8, 9]]
assert minimum_cost(grid) == 12
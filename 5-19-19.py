def number_of_routes(matrix):
    assert len(matrix) > 0
    assert len(matrix[0]) > 0

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    cached = {}
    for i in range(num_rows):
        cached[(i, num_cols)] = 0

    for j in range(num_cols):
        cached[(num_rows, j)] = 0
    
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j]:
                cached[(i, j)] = 0

    cached[(num_rows - 1, num_cols - 1)] = 1

    def nor_dp(i, j):
        key = (i, j)
        if key not in cached:
            cached[key] = nor_dp(i + 1, j) + nor_dp(i, j + 1)
        return cached[key]

    return nor_dp(0, 0)

matrix = [[0, 0, 1],
          [0, 0, 1],
          [1, 0, 0]]
assert number_of_routes(matrix) == 2

matrix = [[0, 0, 1],
          [1, 0, 1],
          [0, 1, 0]]
assert number_of_routes(matrix) == 0
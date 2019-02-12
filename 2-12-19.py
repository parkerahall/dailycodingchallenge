def num_paths(matrix):
    assert len(matrix) > 0
    assert len(matrix[0]) > 1

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    cached = {}
    for i in range(num_rows):
        cached[(i, num_cols - 1)] = 1
    for j in range(num_cols):
        cached[(num_rows - 1, j)] = 1

    def num_paths_dp(i, j):
        if (i, j) not in cached:
            go_right = num_paths_dp(i, j + 1)
            go_down = num_paths_dp(i + 1, j)
            cached[(i, j)] = go_right + go_down
        return cached[(i, j)]

    return num_paths_dp(0, 0)

def make_matrix(num_rows, num_cols):
    return [[0] * num_cols for _ in range(num_rows)]

matrix = make_matrix(2, 2)
assert num_paths(matrix) == 2

matrix = make_matrix(3, 2)
assert num_paths(matrix) == 3

matrix = make_matrix(5, 5)
assert num_paths(matrix) == 70
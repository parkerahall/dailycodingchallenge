def columns_to_remove(matrix):
    assert len(matrix) > 0
    assert len(matrix[0]) > 0

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    to_remove = 0
    for col in range(num_cols):
        curr = matrix[0][col]
        for row in range(1, num_rows):
            if matrix[row][col] < curr:
                to_remove += 1
                break
            else:
                curr = matrix[row][col]
    return to_remove

matrix = [['c', 'b', 'a'], ['d', 'a', 'f'], ['g', 'h', 'i']]
assert columns_to_remove(matrix) == 1

matrix = [['c', 'a'], ['d', 'f'], ['g', 'i']]
assert columns_to_remove(matrix) == 0

matrix = [['a', 'b', 'c', 'd', 'e', 'f']]
assert columns_to_remove(matrix) == 0

matrix = [['z', 'y', 'x'], ['w', 'v', 'u'], ['t', 's', 'r']]
assert columns_to_remove(matrix) == 3
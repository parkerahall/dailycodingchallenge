# uses O(N^2) extra space
def rotate_easy(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    new_matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    for i in range(num_rows):
        col_index = num_cols - i - 1
        for j in range(num_cols):
            new_matrix[j][col_index] = matrix[i][j]
    
    for i in range(num_rows):
        matrix[i] = new_matrix[i]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
expected = [[7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]]
rotate_easy(matrix)
assert matrix == expected

def rotate_coords(N, coord):
    y, new_y = coord
    new_x = N - y - 1
    return new_y, new_x

def top_to_right(N, top):
    return rotate_coords(N, top)

def top_to_bottom(N, top):
    for _ in range(2):
        top = rotate_coords(N, top)
    return top

def top_to_left(N, top):
    for _ in range(3):
        top = rotate_coords(N, top)
    return top

# uses O(1) extra space
def rotate_hard(matrix):
    N = len(matrix)
    for i in range(N / 2):
        for j in range(i, N - i - 1):
            y, x = i, j
            for _ in range(3):
                y, x = rotate_coords(N, (y, x))
                matrix[i][j], matrix[y][x] = matrix[y][x], matrix[i][j]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
expected = [[7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]]
rotate_hard(matrix)
assert matrix == expected
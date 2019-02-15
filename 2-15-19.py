def move(i, j, direction):
    direction_dict = { "U": (-1, 0),
                       "D": (1, 0),
                       "L": (0, -1),
                       "R": (0, 1) }
    i_diff, j_diff = direction_dict[direction]
    return i + i_diff, j + j_diff

def print_matrix_clockwise(matrix):
    assert len(matrix) > 0
    assert len(matrix[0]) > 0

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    num_elts = num_rows * num_cols

    pad_top = 0
    pad_bottom = 0
    pad_left = 0
    pad_right = 0

    count = 0
    curr_i, curr_j = 0, -1
    direction = "R"
    while count < num_elts:
        curr_i, curr_j = move(curr_i, curr_j, direction)
        print matrix[curr_i][curr_j]
        if direction == "R" and curr_j >= num_cols - pad_right - 1:
            direction = "D"
            pad_top += 1
        elif direction == "D" and curr_i >= num_rows - pad_bottom - 1:
            direction = "L"
            pad_right += 1
        elif direction == "L" and curr_j <= pad_left:
            direction = "U"
            pad_bottom += 1
        elif direction == "U" and curr_i <= pad_top:
            direction = "R"
            pad_top += 1
        count += 1

matrix = [ [1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20] ]
print_matrix_clockwise(matrix)
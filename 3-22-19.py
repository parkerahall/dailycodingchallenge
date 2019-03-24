def number_of_steps(points):
    if len(points) == 0:
        return 0

    total = 0
    current = points[0]
    for i in range(1, len(points)):
        curr_row, curr_col = current
        nxt_row, nxt_col = points[i]
        row_diff = abs(nxt_row - curr_row)
        col_diff = abs(nxt_col - curr_col)
        total += min(row_diff, col_diff) + abs(row_diff - col_diff)

        current = points[i]
    return total

points = [(0, 0), (1, 1), (1, 2)]
assert number_of_steps(points) == 2
assert number_of_steps(points[::-1]) == 2
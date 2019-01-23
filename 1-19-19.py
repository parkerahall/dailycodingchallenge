def n_queens(n):

    def n_queens_recursive(queens):
        if len(queens) == n:
            return 1

        total = 0
        new_col = len(queens)
        for new_row in range(n):
            valid = True
            for prev_col in range(new_col):
                prev_row = queens[prev_col]
                if new_row == prev_row or abs(new_row - prev_row) == abs(new_col - prev_col):
                    valid = False
                    break
            if valid:
                queens.append(new_row)
                total += n_queens_recursive(queens)
                queens.pop()
        return total

    return n_queens_recursive([])

n = 5
assert n_queens(n) == 10

n = 6
assert n_queens(n) == 4

n = 7
assert n_queens(n) == 40

n = 8
assert n_queens(n) == 92

n = 9
assert n_queens(n) == 352

n = 10
assert n_queens(n) == 724
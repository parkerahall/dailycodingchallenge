def make_valid_moves(N):
    valid_moves = {}
    for i in range(N):
        for j in range(N):
            moves = []
            for i_diff in [-1, 1]:
                for j_diff in [-2, 2]:
                    new_i, new_j = i + i_diff, j + j_diff
                    if new_i >= 0 and new_i < N and new_j >= 0 and new_j < N:
                        moves.append((new_i, new_j))
            for i_diff in [-2, 2]:
                for j_diff in [-1, 1]:
                    new_i, new_j = i + i_diff, j + j_diff
                    if new_i >= 0 and new_i < N and new_j >= 0 and new_j < N:
                        moves.append((new_i, new_j))
            valid_moves[(i, j)] = moves
    return valid_moves

def knights_tour(N):
    board = [[0] * N for _ in range(N)]
    valid_moves = make_valid_moves(N)

    def kt_recursive(board, i, j, num_moves):
        if num_moves == len(board) ** 2 - 1:
            return 1

        board[i][j] = 1
        total = 0
        for next_i, next_j in valid_moves[(i, j)]:
            if board[next_i][next_j] == 0:
                total += kt_recursive(board, next_i, next_j, num_moves + 1)
        board[i][j] = 0
        return total

    total = 0
    for start_i in range(N):
        for start_j in range(N):
            total += kt_recursive(board, start_i, start_j, 0)
    return total

expected = [1, 0, 0, 0, 1728]
for i in range(len(expected)):
    N = i + 1
    assert knights_tour(N) == expected[i]
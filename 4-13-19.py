def max_coins(board):
    assert len(board) > 0
    assert len(board[0]) > 0

    num_rows = len(board)
    num_cols = len(board[0])

    memo = {}
    memo[(num_rows - 1, num_cols - 1)] = board[num_rows - 1][num_cols - 1]

    def max_coins_dp(i, j):
        if (i, j) not in memo:
            go_down = max_coins_dp(i + 1, j) if (i + 1) < num_rows else -float('inf')
            go_right = max_coins_dp(i, j + 1) if (j + 1) < num_cols else -float('inf')
            answer = board[i][j] + max(go_down, go_right)
            memo[(i, j)] = answer
        return memo[(i, j)]

    return max_coins_dp(0, 0)

board = [[0, 3, 1, 1],
         [2, 0, 0, 4],
         [1, 5, 3, 1]]
expected = 12
assert max_coins(board) == expected
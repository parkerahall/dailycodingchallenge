BOARD_WIDTH = 9
BOARD_SIZE = BOARD_WIDTH ** 2

BOXES_TL_CORNERS = [ 0,               BOARD_WIDTH / 3,      2 * BOARD_WIDTH / 3, 
                     3 * BOARD_WIDTH, 10 * BOARD_WIDTH / 3, 11 * BOARD_WIDTH / 3,
                     6 * BOARD_WIDTH, 19 * BOARD_WIDTH / 3, 20 * BOARD_WIDTH / 3 ]

NUMBERS = [i for i in range(1, BOARD_WIDTH + 1)]

def check_rows(board):
    for row in range(BOARD_WIDTH):
        available = set(NUMBERS)
        for col in range(BOARD_WIDTH):
            index = row * BOARD_WIDTH + col
            number = board[index]
            if number > 0:
                if number in available:
                    available.remove(number)
                else:
                    return False
    return True

def check_cols(board):
    for col in range(BOARD_WIDTH):
        available = set(NUMBERS)
        for row in range(BOARD_WIDTH):
            index = row * BOARD_WIDTH + col
            number = board[index]
            if number > 0:
                if number in available:
                    available.remove(number)
                else:
                    return False
    return True

def check_bxes(board):
    for tl_corner in BOXES_TL_CORNERS:
        available = set(NUMBERS)
        for dx in [0, 1, 2]:
            for dy in [0, 1, 2]:
                index = tl_corner + dx + dy * BOARD_WIDTH
                number = board[index]
                if number > 0:
                    if number in available:
                        available.remove(number)
                    else:
                        return False
    return True

def get(lst, ind, default):
    if ind < len(lst) and ind >= 0:
        return lst[ind]
    return default

def sudoku_solver(board, next_empty):
    good_rows = check_rows(board)
    good_cols = check_cols(board)
    good_bxes = check_bxes(board)
    if good_rows and good_cols and good_bxes:
        next_next_empty = next_empty + 1
        while get(board, next_next_empty, 0) != 0:
            next_next_empty += 1

        if next_next_empty > BOARD_SIZE:
            return True
        
        for i in NUMBERS:
            board[next_empty] = i
            solved = sudoku_solver(board, next_next_empty)
            if solved:
                return True
            board[next_empty] = 0
    return False

def pretty_print_board(board):
    for i in range(BOARD_WIDTH):
        print board[i * BOARD_WIDTH: (i + 1) * BOARD_WIDTH]

board = [0] * BOARD_SIZE
assert sudoku_solver(board, 0)
pretty_print_board(board)
            
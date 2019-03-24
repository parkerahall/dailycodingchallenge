cached_board = None
cached_graph = None

def make_graph(board):
    def in_bounds(row, col):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

    graph = {}
    letters = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            letter = board[i][j]
            if letter not in letters:
                letters[letter] = []

            letters[letter].append((i, j))
            graph[(i, j)] = {}
            for neighbor_row, neighbor_col in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if in_bounds(neighbor_row, neighbor_col):
                    neighbor_letter = board[neighbor_row][neighbor_col]
                    if neighbor_letter not in graph[(i, j)]:
                        graph[(i, j)][neighbor_letter] = []

                    graph[(i, j)][neighbor_letter].append((neighbor_row, neighbor_col))

    return graph, letters

def find(graph, current, string, used):
    if len(string) == 0:
        return True
    
    found = False
    for nxt in graph[current].get(string[0], []):
        if nxt not in used:
            new_used = used.copy()
            new_used.add(nxt)
            found = found or find(graph, nxt, string[1:], new_used)
    return found

def exists(board, string):
    global cached_board
    global cached_graph
    if cached_board == board:
        graph, letters = cached_graph
    else:
        graph, letters = make_graph(board)
    cached_board = board
    cached_graph = (graph, letters)

    found = False
    for start in letters.get(string[0], []):
        used = set([start])
        found = found or find(graph, start, string[1:], used)
    return found

board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]

string = "ABCCED"
assert exists(board, string) == True

string = "SEE"
assert exists(board, string) == True

string = "ABCB"
assert exists(board, string) == False
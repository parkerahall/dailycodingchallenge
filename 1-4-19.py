#left, right, up, down
MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def is_neighbor(board, i, j):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return False
    return not board[i][j]

def convert_to_graph(board):
    assert len(board) > 0
    assert len(board[0]) > 0

    num_rows = len(board)
    num_cols = len(board[0])

    neighbors = {}
    for i in range(num_rows):
        for j in range(num_cols):
            neighbors[(i, j)] = []
            for diff_i, diff_j in MOVES:
                new_i = i + diff_i
                new_j = j + diff_j
                if is_neighbor(board, new_i, new_j):
                    neighbors[(i, j)].append((new_i, new_j))
    return neighbors

def BFS(graph, start):
    queue = [start]
    levels = {start : 0}
    while len(queue) > 0:
        new_queue = []
        for node in queue:
            for neighbor in graph[node]:
                if neighbor not in levels:
                    new_queue.append(neighbor)
                    levels[neighbor] = levels[node] + 1
        queue = new_queue
    return levels

def min_steps(board, start, end):
    graph = convert_to_graph(board)
    levels = BFS(graph, start)
    return levels[end]


board = [[False, False, False, False],
         [True, True, False, True],
         [False, False, False, False],
         [False, False, False, False]]
start = (3, 0)
end = (0, 0)
assert min_steps(board, start, end) == 7
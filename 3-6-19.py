def get(matrix, row, col):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0
    return matrix[row][col]

def neighbors(row, col):
    n = []
    diffs = [-1, 0, 1]
    for dx in diffs:
        for dy in diffs:
            n.append((row + dx, col + dy))
    return n

def make_adjacency(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    adjacency = {}
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j]:
                adjacency[(i, j)] = set()
                for nx, ny in neighbors(i, j):
                    if get(matrix, nx, ny):
                        adjacency[(i, j)].add((nx, ny))
    return adjacency


def DFS_visit(adjacency, node, visited):
    for neighbor in adjacency[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            DFS_visit(adjacency, neighbor, visited)

def DFS(adjacency):
    visited = set()
    connected = 0
    for node in adjacency:
        if node not in visited:
            visited.add(node)
            DFS_visit(adjacency, node, visited)
            connected += 1
    return connected

def count_islands(matrix):
    assert len(matrix) > 0
    assert len(matrix[0]) > 0
    adjacency = make_adjacency(matrix)
    return DFS(adjacency)

matrix = [[1, 0, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 1, 0, 0, 1],
          [1, 1, 0, 0, 1]]
assert count_islands(matrix) == 4
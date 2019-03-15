def reverse_edges(adjacency):
    reverse_adj = {node : set() for node in adjacency}
    starts = []
    for node in adjacency:
        if len(adjacency[node]) == 0:
            starts.append(node)

        for adjacent_node in adjacency[node]:
            reverse_adj[adjacent_node].add(node)
    return reverse_adj, starts

def DFS(adjacency, starts):
    ordering = []
    total_visited = set()

    def DFS_visit(adjacency, start, visited):
        if start in total_visited:
            return False

        visited.add(start)
        total_visited.add(start)
        for node in adjacency[start]:
            if node in visited:
                return True
            DFS_visit(adjacency, node, visited.copy())
        ordering.append(start)
        return False

    for start in starts:
        has_cycle = DFS_visit(adjacency, start, set([start]))
        if has_cycle:
            return None

    return ordering[::-1]


def class_ordering(prereqs):
    adjacency, starts = reverse_edges(prereqs)
    return DFS(adjacency, starts)

prereqs = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
assert class_ordering(prereqs) == ['CSC100', 'CSC200', 'CSC300']
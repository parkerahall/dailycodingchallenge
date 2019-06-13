def is_minimally_connected(graph):
    source = min(graph)

    visited = set([source])
    frontier = [source]
    parent = {source : None}

    while len(frontier) > 0:
        new_frontier = []
        for node in frontier:
            for neighbor in graph[node]:
                if neighbor in visited and neighbor != parent[node]:
                    # cycle detected
                    return False
                elif neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    new_frontier.append(neighbor)
        frontier = new_frontier
    return len(visited) == len(graph)

graph = {0 : [1, 2, 4],
         1 : [0, 3, 5],
         2 : [0],
         3 : [1],
         4 : [0],
         5 : [1]}
assert is_minimally_connected(graph) == True

graph = {0 : [1, 2, 4],
         1 : [0, 3, 5],
         2 : [0],
         3 : [1],
         4 : [0],
         5 : [1]}
for i in range(6):
    for j in range(6):
        if i != j:
            graph[i].append(j)
            graph[j].append(i)
            assert is_minimally_connected(graph) == False
            graph[i].pop()
            graph[j].pop()
# asymptotic runtime is O(kV + E)
def coloring_problem(adjacency, k):
    colors = {vertex : k for vertex in adjacency}

    frontier = [adjacency.keys()[0]]
    while len(frontier) > 0:
        new_frontier = []
        for vertex in frontier:
            available_colors = set(range(k))
            seen_colors = set()
            for adjacent in adjacency[vertex]:
                set_color = colors[adjacent]
                if set_color < k:
                    seen_colors.add(set_color)
                else:
                    new_frontier.append(adjacent)
            available_colors -= seen_colors
            if len(available_colors) == 0:
                return False
            else:
                colors[vertex] = min(available_colors)
        frontier = new_frontier
    return True

adjacency = { 0 : [1, 2],
              1 : [0, 2],
              2 : [0, 1] }
k = 2
assert coloring_problem(adjacency, k) == False

adjacency = { 0 : [1, 2],
              1 : [0, 2],
              2 : [0, 1] }
k = 3
assert coloring_problem(adjacency, k) == True

adjacency = { 0 : [1, 2],
              1 : [0, 3],
              2 : [0, 3],
              3 : [1, 2] }
k = 2
assert coloring_problem(adjacency, k) == True
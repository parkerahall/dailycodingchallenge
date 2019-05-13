NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def set_grid(grid, loc, color):
    grid[loc[1]][loc[0]] = color

def get_from_grid(grid, loc, default=-1):
    x, y = loc
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return default
    return grid[y][x]

def same_color_neighbors(grid):
    neighbor_dict = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            loc = (row, col)
            loc_color = get_from_grid(grid, loc)
            same_colors = []
            for n in NEIGHBORS:
                neighbor_loc = (loc[0] + n[0], loc[1] + n[1])
                if get_from_grid(grid, neighbor_loc) == loc_color:
                    same_colors.append(neighbor_loc)
            neighbor_dict[loc] = same_colors
    return neighbor_dict

def color_fill(grid, loc, color):
    same_neighbors = same_color_neighbors(grid)
    
    seen = set()
    current = [loc]
    while len(current) > 0:
        new = []
        for curr_loc in current:
            if curr_loc not in seen:
                set_grid(grid, curr_loc, color)
                new.extend(same_neighbors[curr_loc])
                seen.add(curr_loc)
        current = new

grid = [['B', 'B', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B']]
loc = (2, 2)
color = 'G'
color_fill(grid, loc, color)
print(grid)
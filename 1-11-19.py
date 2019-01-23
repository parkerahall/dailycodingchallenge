def rain(walls):
    highest = -1
    partial_total = 0
    total = 0
    for wall in walls:
        if wall >= highest:
            highest = wall
            total += partial_total
            partial_total = 0
        else:
            partial_total += (highest - wall)
    return total

walls = [2, 1, 2]
assert rain(walls) == 1

walls = [3, 0, 1, 3, 0, 5]
assert rain(walls) == 8

walls = [3, 0, 1, 3, 0]
assert rain(walls) == 5
def is_overlapping(rect1, rect2):
    corner1 = rect1["top_left"]
    dims1 = rect1["dimensions"]

    corner2 = rect2["top_left"]
    dims2 = rect2["dimensions"]

    if corner1[0] + dims1[0] <= corner2[0] or corner2[0] + dims2[0] <= corner1[0]:
        return False

    if corner1[1] + dims1[1] <= corner2[1] or corner2[1] + dims2[1] <= corner1[1]:
        return False

    return True

def any_pair_overlaps(rectangles):
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if is_overlapping(rectangles[i], rectangles[j]):
                return True
    return False

rectangles = [{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}]
assert any_pair_overlaps(rectangles) == True

rectangles = [{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (5, 10),
    "dimensions": (4, 3)
}]
assert any_pair_overlaps(rectangles) == False
def length_of_intersection(range1, range2):
    return max(min(range1[1], range2[1]) - max(range1[0], range2[0]), 0)

def area_of_interesection(rect1, rect2):
    left_1, top_1 = rect1["top_left"]
    width_1, height_1 = rect1["dimensions"]
    right_1, bottom_1 = left_1 + width_1, top_1 + height_1

    left_2, top_2 = rect2["top_left"]
    width_2, height_2 =  rect2["dimensions"]
    right_2, bottom_2 = left_2 + width_2, top_2 + height_2

    x_intersection = length_of_intersection((left_1, right_1), (left_2, right_2))
    y_intersection = length_of_intersection((top_1, bottom_1), (top_2, bottom_2))
    return x_intersection * y_intersection

rect1 = {"top_left": (1, 4), "dimensions": (3, 3)}
rect2 = {"top_left": (0, 5), "dimensions": (4, 3)}
assert area_of_interesection(rect1, rect2) == 6

rect1 = {"top_left": (0, 0), "dimensions": (3, 3)}
rect2 = {"top_left": (2, 3), "dimensions": (4, 3)}
assert area_of_interesection(rect1, rect2) == 0
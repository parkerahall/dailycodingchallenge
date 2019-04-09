def square_sort(integers):
    return sorted([x ** 2 for x in integers])

integers = [-9, -2, 0, 2, 3]
expected = [0, 4, 4, 9, 81]
assert square_sort(integers) == expected
def longest_consecutive_sequence(array):
    if len(array) == 0:
        return 0

    best = 0
    elts = set(array)
    for elt in array:
        count = 0
        if elt - 1 not in elts:
            while elt in array:
                elt += 1
                count += 1
        best = max(best, count)
    return best

array = [100, 4, 200, 1, 3, 2]
assert longest_consecutive_sequence(array) == 4
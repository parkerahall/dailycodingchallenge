def find_duplicate(lst):
    arr = [0] * (len(lst) - 1)
    for elt in lst:
        if arr[elt - 1]:
            return elt
        arr[elt - 1] = 1

lst = [1, 2, 3, 4, 5, 5]
assert find_duplicate(lst) == 5

lst = [1, 4, 9, 8, 4, 2, 3, 5, 6, 7]
assert find_duplicate(lst) == 4
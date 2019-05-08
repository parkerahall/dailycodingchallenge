def reverse(lst, i, j):
    lst[i:j + 1] = lst[i:j + 1][::-1]

def find_min(lst, start):
    min_index = start
    min_value = lst[start]
    for i in range(start, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = i
    return min_index

def sort_with_reverse(lst):
    for start in range(len(lst)):
        min_index = find_min(lst, start)
        reverse(lst, start, min_index)

lst = [4, 5, 3, 2, 7, -1, 12]
expected = sorted(lst)
sort_with_reverse(lst)
assert expected == lst
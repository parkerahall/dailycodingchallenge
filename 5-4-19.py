def pivot_partition(lst, x):
    more = len(lst) - 1
    not_more = 0

    i = 0
    while i <= more:
        if lst[i] > x:
            lst[i], lst[more] = lst[more], lst[i]
            more -= 1
        else:
            i += 1

    less = 0
    equal = i - 1

    j = 0
    while j <= equal:
        if lst[j] == x:
            lst[j], lst[equal] = lst[equal], lst[j]
            equal -= 1
        else:
            j += 1

def valid_partition(lst, x):
    i = 0
    while i < len(lst) and lst[i] < x:
        i += 1

    while i < len(lst) and lst[i] == x:
        i += 1

    while i < len(lst) and lst[i] > x:
        i += 1

    return i == len(lst)

lst = [9, 12, 3, 5, 14, 10, 10]
x = 10
pivot_partition(lst, x)
assert valid_partition(lst, x) == True
def find_rotation_amount(array, start, end):
    if end - start == 1:
        return end

    mid = (start + end) / 2
    if array[mid] > array[-1]:
        return find_rotation_amount(array, mid, end)
    else:
        return find_rotation_amount(array, start, mid)

def binary_search(array, elt, start, end):
    if array[start] == elt:
        return start
    elif end - start == 1:
        return None

    mid = (start + end) / 2
    if array[mid] > elt:
        return binary_search(array, elt, start, mid)
    else:
        return binary_search(array, elt, mid, end)

def find_elt_in_rotated_array(array, elt):
    last_ind = len(array) - 1
    
    split_ind = find_rotation_amount(array, 0, last_ind)
    
    left_ind = binary_search(array, elt, 0, split_ind - 1)
    right_ind = binary_search(array, elt, split_ind, last_ind)

    if left_ind != None:
        return left_ind

    if right_ind != None:
        return right_ind

    return None

array = [13, 18, 25, 2, 8, 10]
elt = 8
assert find_elt_in_rotated_array(array, elt) == 4

array = [13, 18, 25, 2, 8, 10]
elt = 4
assert find_elt_in_rotated_array(array, elt) == None
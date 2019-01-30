def maximum_contiguous_subarray_sum(array):
    modified = []
    for elt in array:
        if len(modified) == 0:
            modified.append(elt)
            continue

        if modified[-1] * elt >= 0:
            modified[-1] += elt
        else:
            modified.append(elt)
    
    max_sum = 0
    current_sum = 0
    for elt in modified:
        if current_sum + elt > 0:
            current_sum += elt
            max_sum = max(max_sum, current_sum)
        else:
            current_sum = 0
    return max_sum

array = [34, -50, 42, 14, -5, 86]
assert maximum_contiguous_subarray_sum(array) == 137

array = [-5, -1, -8, -9]
assert maximum_contiguous_subarray_sum(array) == 0
def merge_sort_with_inversion_count(array):
    if len(array) == 1:
        return array, 0

    half = len(array) / 2
    left_sorted, left_inversions = merge_sort_with_inversion_count(array[:half])
    right_sorted, right_inversions = merge_sort_with_inversion_count(array[half:])

    output = []
    left_index = 0
    right_index = 0
    merge_inversions = 0
    while left_index < len(left_sorted) and right_index < len(right_sorted):
        if left_sorted[left_index] <= right_sorted[right_index]:
            output.append(left_sorted[left_index])
            left_index += 1
        else:
            output.append(right_sorted[right_index])
            right_index += 1
            merge_inversions += (len(left_sorted) - left_index)

    for i in range(left_index, len(left_sorted)):
        output.append(left_sorted[i])

    for i in range(right_index, len(right_sorted)):
        output.append(right_sorted[i])

    return output, (left_inversions + right_inversions + merge_inversions)

def num_inversions(array):
    sorted_array, inversion_count = merge_sort_with_inversion_count(array)

    return inversion_count

array = [2, 4, 1, 3, 5]
assert num_inversions(array) == 3

array = [5, 4, 3, 2, 1]
assert num_inversions(array) == 10
def reverse_in_place(arr, start, end):
    if start > end:
        return arr

    arr[end], arr[start] = arr[start], arr[end]
    reverse_in_place(arr, start + 1, end - 1)

def next_greater_permutation(digits):
    if len(digits) == 0:
        return digits

    index = len(digits) - 2
    while index >= 0 and digits[index + 1] < digits[index]:
        index -= 1

    if index < 0:
        return digits[::-1]

    next_highest = float('inf')
    next_highest_ind = -1
    for i in range(index + 1, len(digits)):
        if digits[i] > digits[index] and digits[i] < next_highest:
            next_highest = digits[i]
            next_highest_ind = i

    digits[index], digits[next_highest_ind] = digits[next_highest_ind], digits[index]
    reverse_in_place(digits, index + 1, len(digits) - 1)

    return digits


digits = [3, 2, 1]
expected = [1, 2, 3]
assert next_greater_permutation(digits) == expected

digits = [5, 4, 3, 2, 1]
expected = [1, 2, 3, 4, 5]
assert next_greater_permutation(digits) == expected

digits = [1, 5, 4, 2]
expected = [2, 1, 4, 5]
assert next_greater_permutation(digits) == expected

digits = [1, 2, 3]
expected = [1, 3, 2]
assert next_greater_permutation(digits) == expected

digits = [1, 3, 2]
expected = [2, 1, 3]
assert next_greater_permutation(digits) == expected

digits = [3, 5, 4, 2, 1]
expected = [4, 1, 2, 3, 5]
assert next_greater_permutation(digits) == expected
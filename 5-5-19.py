def find_closest_largest(arr, i):
    small = arr[i]
    
    left = i - 1
    right = i + 1
    while left >= 0 or right < len(arr):
        if left >= 0 and arr[left] > small:
            return left

        if right < len(arr) and arr[right] > small:
            return right

        left -= 1
        right += 1

    return None

arr = [4, 1, 3, 5, 6]
i = 0
assert find_closest_largest(arr, i) == 3

arr = [1, 5, 6, 1, 2, 2, 7]
i = 4
expected = set([2, 6])
assert find_closest_largest(arr, i) in expected

def preprocess_arr(arr):
    length = len(arr)
    
    left_closest = [float('inf')] * length
    left_stack = []

    right_closest = [-float('inf')] * length
    right_stack = []
    
    for left_ind in range(length):
        right_ind = length - left_ind - 1
        
        while len(left_stack) > 0 and arr[left_ind] > arr[left_stack[-1]]:
            j = left_stack.pop()
            left_closest[j] = left_ind
        left_stack.append(left_ind)

        while len(right_stack) > 0 and arr[right_ind] > arr[right_stack[-1]]:
            j = right_stack.pop()
            right_closest[j] = right_ind
        right_stack.append(right_ind)

    closest_largest = []
    for i in range(length):
        if left_closest[i] - i < i - right_closest[i]:
            closest_largest.append(left_closest[i])
        else:
            closest_largest.append(right_closest[i])

    return closest_largest

def find_closest_largest_preprocess(arr, i):
    closest_largest = preprocess_arr(arr)
    return closest_largest[i]

arr = [4, 1, 3, 5, 6]
i = 0
assert find_closest_largest_preprocess(arr, i) == 3

arr = [1, 5, 6, 1, 2, 2, 7]
i = 4
expected = set([2, 6])
assert find_closest_largest_preprocess(arr, i) in expected

arr = [5, 6, 3, 2, 1]
i = 2
assert find_closest_largest_preprocess(arr, i) == 1
def find_contiguous_sum(integers, k):
    start = 0
    end = 0
    total = 0
    while total < k and end < len(integers):
        total += integers[end]
        end += 1
        while total > k:
            total -= integers[start]
            start += 1
    
    if total == k:
        return integers[start:end]
    return None

integers = [1, 2, 3, 4, 5]
k = 9
assert find_contiguous_sum(integers, k) == [2, 3, 4]
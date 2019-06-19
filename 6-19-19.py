def longest_nonrepeating_subsequence(array):
    location = {}
    start = 0
    end = 0
    best = 0
    while end < len(array):
        if array[end] in location and location[array[end]] >= start:
            start = location[array[end]] + 1
        location[array[end]] = end
        end += 1
        best = max(best, end - start)
    return best

array = [5, 1, 3, 5, 2, 3, 4, 1]
assert longest_nonrepeating_subsequence(array) == 5

array = [1, 2, 3, 4, 5, 6]
assert longest_nonrepeating_subsequence(array) == 6

array = [1, 1, 1, 1, 1, 1, 1, 1]
assert longest_nonrepeating_subsequence(array) == 1

array = [1, 2, 2]
assert longest_nonrepeating_subsequence(array) == 2
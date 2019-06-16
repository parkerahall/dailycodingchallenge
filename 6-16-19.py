def min_diff_subsets(numbers):
    smallest = [sum(numbers)]
    best = [None]
    
    def mds_recur(left, right):
        i = len(left) + len(right)
        if i == len(numbers):
            diff = abs(sum(left) - sum(right))
            if diff < smallest[0]:
                best[0] = (left, right)
                smallest[0] = diff
        else:
            new_left = left.copy()
            new_left.add(numbers[i])
            mds_recur(new_left, right)

            new_right = right.copy()
            new_right.add(numbers[i])
            mds_recur(left, new_right)

    mds_recur(set(), set())
    return best[0]

numbers = [5, 10, 15, 20, 25]
expected_diff = 5
first_actual, second_actual = min_diff_subsets(numbers)
assert abs(sum(first_actual) - sum(second_actual)) == expected_diff
# N subproblems, O(N) time per subproblem, O(N) work at the end => O(N^2) runtime
def longest_increasing_subsequence(array):
    cached = {0 : 1}

    def lis_dp(i):
        if i not in cached:
            maximum = 0
            for j in range(i):
                maximum = max(maximum, lis_dp(j) if array[j] < array[i] else 0)
            cached[i] = maximum + 1
        return cached[i]

    return max(lis_dp(i) for i in range(len(array)))

array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
assert longest_increasing_subsequence(array) == 6
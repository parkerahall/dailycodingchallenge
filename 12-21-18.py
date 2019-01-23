# DP solution with O(N) runtime and O(N) space
# def max_nonadjacent(l):
#     cached = {}
#     cached[len(l)] = 0
#     cached[len(l) + 1] = 0
    
#     def max_nonadjacent_dp(index):
#         if index not in cached:
#             cached[index] = max(l[index] + max_nonadjacent_dp(index + 2), max_nonadjacent_dp(index + 1))
#         return cached[index]

#     return max_nonadjacent_dp(0)

# Optimal solution with O(N) runtime and O(1) space
def max_nonadjacent(l):
    max_inclusive = 0
    max_exclusive = 0
    for i in range(len(l)):
        max_inclusive, max_exclusive = max_exclusive + l[i], max(max_exclusive, max_inclusive)
    return max(max_inclusive, max_exclusive)

l = [2, 4, 6, 2, 5]
assert max_nonadjacent(l) == 13

l = [5, 1, 1, 5]
assert max_nonadjacent(l) == 10

l = [3, 5, 4]
assert max_nonadjacent(l) == 7

l = [5, 1, 2, 5, 7]
assert max_nonadjacent(l) == 14

l = [5, 1, 1, 5, 2]
assert max_nonadjacent(l) == 10

l = [5, 0, -2, 3, -5]
assert max_nonadjacent(l) == 8
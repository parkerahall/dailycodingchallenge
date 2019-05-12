def nearest_k_points(center, points, k):
    return sorted(points, key=lambda x: ((x[0] - center[0]) ** 2 + (x[1] - center[1]) ** 2) ** .5)[:k]

center = (1, 2)
points = [(0, 0), (5, 4), (3, 1)]
k = 2
expected = [(0, 0), (3, 1)]
actual = nearest_k_points(center, points, k)
assert set(expected) == set(actual)
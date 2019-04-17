def rotate(l, k):
    length = len(l)
    k = k % length
    for i in range(length - k):
        new_index = (i - k) % length
        l[i], l[new_index] = l[new_index], l[i]

l = [1, 2, 3, 4, 5, 6]
k = 2
expected = [3, 4, 5, 6, 1, 2]
rotate(l, k)
assert l == expected
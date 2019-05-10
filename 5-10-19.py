cached = {}

def preprocess(L):
    running = [sum(L)]
    for elt in L[::-1]:
        running.append(running[-1] - elt)
    return running[::-1]

def subset_sum(L, i, j):
    key = tuple(L)
    if key not in cached:
        cached[key] = preprocess(L)

    running = cached[key]
    return running[j] - running[i]

L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    for j in range(i, len(L)):
        assert sum(L[i:j]) == subset_sum(L, i, j)
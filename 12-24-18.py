# O(N) runtime
def staircase(N):
    cached = {0 : 1, 1 : 1}
    def recurse(N):
        if N not in cached:
            output = recurse(N - 1) + recurse(N - 2)
            cached[N] = output
        return cached[N]
    return recurse(N)

# O(N * |steps|) runtime
def staircase_expanded(N, steps):
    cached = {0 : 1}
    for i in range(max(steps)):
        cached[-(i + 1)] = 0 
    def recurse(N):
        if N not in cached:
            output = sum([recurse(N - i) for i in steps])
            cached[N] = output
        return cached[N]
    return recurse(N)


N = 4
assert staircase(N) == 5

N = 2
assert staircase(N) == 2

N = 1
assert staircase(N) == 1

N = 4
steps = [1, 2]
assert staircase_expanded(N, steps) == 5
import random

def random_without(n, l):
    skip = set(l)
    attempt = random.randint(0, n - 1)
    while attempt in skip:
        attempt = random.randint(0, n - 1)
    return attempt

N = 1000
for _ in range(N):
    without_size = random.randint(0, N - 1)
    without = random.sample(range(N), without_size)
    random_num = random_without(N, without)
    assert random_num >= 0
    assert random_num < N
    assert random_num not in without
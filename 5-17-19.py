def smallest_square_sum(n):
    if n == 0:
        return 1
    
    cached = {i ** 2 : 1 for i in range(1, int(n ** .5) + 1)}
    cached[0] = 0

    def sss_dp(m):
        if m not in cached:
            smallest = m - 1
            for i in range(2, int(m ** .5) + 1):
                smallest = min(smallest, sss_dp(m - i ** 2))
            cached[m] = smallest + 1
        return cached[m]

    return sss_dp(n)

for i in range(100):
    assert smallest_square_sum(i ** 2) == 1

n = 13
assert smallest_square_sum(n) == 2

n = 27
assert smallest_square_sum(n) == 3
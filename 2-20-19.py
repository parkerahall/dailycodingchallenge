def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n /= 10
    return total

def nth_perfect(n):
    remaining = 10 - digit_sum(n)
    return 10 * n + remaining

expected = [19, 28, 37, 46, 55, 64, 73, 82, 91, 109, 118, 127]
for i in range(len(expected)):
    assert nth_perfect(i + 1) == expected[i]
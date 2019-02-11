def exponentiation(base, power):
    if power == 0:
        return 1

    half = power / 2
    square_root = exponentiation(base, half)
    answer = square_root * square_root * (base if power % 2 else 1)
    return answer

base = 2
power = 10
assert exponentiation(base, power) == 1024

base = 3
power = 7
assert exponentiation(base, power) == 2187
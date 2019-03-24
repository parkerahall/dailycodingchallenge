def is_prime(number):
    for factor in range(2, int(number ** .5) + 1):
        if number % factor == 0:
            return False
    return True

def prime_sum(number):
    for a in range(2, number / 2 + 1):
        if is_prime(a) and is_prime(number - a):
            return a, number - a

number = 4
assert prime_sum(number) == (2, 2)

number = 6
assert prime_sum(number) == (3, 3)

number = 8
assert prime_sum(number) == (3, 5)

number = 10
assert prime_sum(number) == (3, 7)

number = 12
assert prime_sum(number) == (5, 7)

number = 100
assert prime_sum(number) == (3, 97)
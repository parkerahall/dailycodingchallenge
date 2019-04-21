def square_root(n):
    root = abs(n) ** .5
    factor = 1j if n < 0 else 1
    return factor * root

n = 9
assert square_root(n) == 3

n = -25./16
assert square_root(n) == 5j/4
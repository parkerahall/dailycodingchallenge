def mult_table_count(n, x):
    return sum([(x % i) == 0 and (x / i) <= n for i in range(1, n + 1)])

n = 6
x = 12
assert mult_table_count(n, x) == 4

n = 12
x = 12
assert mult_table_count(n, x) == 6

n = 10
x = 77
assert mult_table_count(n, x) == 0
ODD_ONES = sum([4 ** n for n in range(4)])
EVEN_ONES = ODD_ONES << 1

def swap_bits(x):
    return ((x & ODD_ONES) << 1) | ((x & EVEN_ONES) >> 1)

x = int('10101010', 2)
expected = int('01010101', 2)
assert swap_bits(x) == expected

x = int('11100010', 2)
expected = int('11010001', 2)
assert swap_bits(x) == expected
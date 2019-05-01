def find_singles(array):
    set_bits = 0
    for elt in array:
        set_bits ^= elt

    # get single bit set
    first_set = set_bits & ~(set_bits - 1)

    start = 0
    end = len(array) - 1
    while start <= end:
        if first_set & array[start]:
            start += 1
        else:
            array[start], array[end] = array[end], array[start]
            end -= 1

    first = 0
    for elt in array[:start]:
        first ^= elt

    second = 0
    for elt in array[start:]:
        second ^= elt

    return first, second


array = [2, 4, 6, 8, 10, 2, 6, 10]
expected = [4, 8]
actual = find_singles(array)
assert set(expected) == set(actual)

array = [2, 4, 6, 7, 10, 2, 6, 10]
expected = [4, 7]
actual = find_singles(array)
assert set(expected) == set(actual)
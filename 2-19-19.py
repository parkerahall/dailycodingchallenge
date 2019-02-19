def largest_three_product(integers):
    first = 0
    second = 0
    third = 0

    neg_first = 0
    neg_second = 0

    for integer in integers:
        if integer > 0:
            if integer > first:
                third = second
                second = first
                first = integer
            elif integer > second:
                third = second
                second = integer
            elif integer > third:
                third = integer
        elif integer < 0:
            if integer < neg_first:
                neg_second = neg_first
                neg_first = integer
            elif integer < neg_second:
                neg_second = integer
    return max(first * second * third, first * neg_first * neg_second)

integers = [-10, -10, 5, 2]
assert largest_three_product(integers) == 500

integers = [-10, -10, 5, 21, 200]
assert largest_three_product(integers) == 21000
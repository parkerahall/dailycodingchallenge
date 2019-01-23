EPS = .001
def is_int(number):
    return abs(number - round(number)) < EPS

def non_duplicated_attempt(trips):
    num_zeros = 0
    product = 1.
    for elt in trips:
        if elt == 0:
            num_zeros += 1
        else:
            product *= elt

    if num_zeros == 1:
        return 0

    for elt in trips:
        remaining = product / elt
        if is_int(remaining ** (1./3)):
            return elt

trips = [6, 1, 3, 3, 3, 6, 6]
assert non_duplicated_attempt(trips) == 1

trips = [13, 19, 13, 13]
assert non_duplicated_attempt(trips) == 19

# problem arises when every element in list is a perfect cube
# trips = [27, 8, 27, 27]
# assert non_duplicated_attempt(trips) == 8

def non_duplicated(trips):
    ones = 0
    twos = 0

    for number in trips:
        second_appearance = ones & number
        twos ^= second_appearance

        # set bits in 
        ones ^= number

        third_appearance = ones & twos

        ones &= ~third_appearance
        twos &= ~third_appearance

    return ones

trips = [6, 1, 3, 3, 3, 6, 6]
assert non_duplicated(trips) == 1

trips = [13, 19, 13, 13]
assert non_duplicated(trips) == 19

trips = [27, 8, 27, 27]
assert non_duplicated(trips) == 8
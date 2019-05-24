FIRST_LEFT = 0b11111111111111110000000000000000
FIRST_RIGHT = FIRST_LEFT >> 16
SECOND_LEFT = 0b11111111000000001111111100000000
SECOND_RIGHT = SECOND_LEFT >> 8
THIRD_LEFT = 0b11110000111100001111000011110000
THIRD_RIGHT = THIRD_LEFT >> 4
FOURTH_LEFT = 0b11001100110011001100110011001100
FOURTH_RIGHT = FOURTH_LEFT >> 2
FIFTH_LEFT = 0b10101010101010101010101010101010
FIFTH_RIGHT = FIFTH_LEFT >> 1

# reverse the bits of a 32-bit integer
def reverse(integer):
    integer = ((integer & FIRST_LEFT) >> 16) | ((integer & FIRST_RIGHT) << 16)
    integer = ((integer & SECOND_LEFT) >> 8) | ((integer & SECOND_RIGHT) << 8)
    integer = ((integer & THIRD_LEFT) >> 4) | ((integer & THIRD_RIGHT) << 4)
    integer = ((integer & FOURTH_LEFT) >> 2) | ((integer & FOURTH_RIGHT) << 2)
    integer = ((integer & FIFTH_LEFT) >> 1) | ((integer & FIFTH_RIGHT) << 1)
    return integer

integer = 0b11110000111100001111000011110000
expected = int(bin(integer)[2:][::-1], 2)
assert reverse(integer) == expected

integer = 0b10101101010110110101010000011111
expected = int(bin(integer)[2:][::-1], 2)
assert reverse(integer) == expected
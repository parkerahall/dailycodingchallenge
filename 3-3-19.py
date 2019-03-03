def cartesian_product(ranges):
    previous = [[]]
    for rng in ranges:
        new = []
        for term in rng:
            for prev in previous:
                new.append(prev + [term])
        previous = new
    return ["".join(term) for term in previous]

def possible_characters(digits_to_letters, digit_string):
    ranges = []
    for digit in digit_string:
        ranges.append(digits_to_letters[digit])
    return cartesian_product(ranges)

digits_to_letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"]}
digit_string = "23"
expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
actual = possible_characters(digits_to_letters, digit_string)
assert set(expected) == set(actual)
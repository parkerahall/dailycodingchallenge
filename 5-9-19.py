def generate_gray_code(n):
    total = 2 ** n
    digits = []
    for i in range(n):
        first_and_last = total / (2 ** (i + 1))
        middle_split = 2 ** i - 1
        middle_amount = (total - 2 * first_and_last) / middle_split if middle_split > 0 else 0

        place = []
        digit = 0
        for _ in range(first_and_last):
            place.append(digit)

        for j in range(middle_split):
            digit = (digit + 1) % 2
            for _ in range(middle_amount):
                place.append(digit)

        for _ in range(first_and_last):
            place.append((digit + 1) % 2)

        digits.append(place)

    output = []
    for i in range(total):
        output.append(''.join([str(digits[j][i]) for j in range(n)]))

    return output

def check_gray_code(n, values):
    expected_length = 2 ** n
    if len(values) != expected_length or len(set(values)) != expected_length:
        return False

    for i in range(len(values) - 1):
        curr = values[i]
        nxt = values[i + 1]
        diff = 0
        for ind in range(len(curr)):
            if curr[ind] != nxt[ind]:
                diff += 1
            if diff > 1:
                return False

    return True

assert check_gray_code(2, ['00', '01', '10', '11']) == False
assert check_gray_code(3, ['000', '001', '010', '010', '011', '100', '101', '110', '111']) == False

for n in range(2, 6):
    values = generate_gray_code(n)
    assert check_gray_code(n, values) == True
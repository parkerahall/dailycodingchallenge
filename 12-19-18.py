valid = {"": 1}

def num_valid(encoded):
    if encoded in valid:
        return valid[encoded]

    digit = int(encoded[0])
    rest = encoded[1:]

    output = num_valid(rest)
    
    if len(rest) > 0:
        next_digit = int(encoded[1])
        if (digit == 1) or (digit == 2 and next_digit < 7):
            output += num_valid(rest[1:])

    valid[encoded] = output
    return output

encoded = "111"
assert num_valid(encoded) == 3
def is_valid_matching(parens):
    lo = 0
    hi = 0
    for paren in parens:
        if paren == "(":
            lo += 1
            hi += 1
        elif paren == ")":
            lo -= 1
            hi -= 1
        else:
            lo -= 1
            hi += 1
        if hi < 0:
            return False
    return lo <= 0 and 0 <= hi

parens = "(()*"
assert is_valid_matching(parens) == True

parens = "(*)"
assert is_valid_matching(parens) == True

parens = ")*("
assert is_valid_matching(parens) == False

parens = "(()))("
assert is_valid_matching(parens) == False
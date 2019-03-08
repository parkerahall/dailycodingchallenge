def num_to_remove(parentheses):
    num_open = 0
    to_remove = 0
    for paren in parentheses:
        if paren == "(":
            num_open += 1
        elif paren == ")":
            if num_open > 0:
                num_open -= 1
            else:
                to_remove += 1
        else:
            raise "INVALID CHARACTER IN PARENTHESES STRING"
    return to_remove + num_open

parentheses = "()())()"
assert num_to_remove(parentheses) == 1

parentheses = ")("
assert num_to_remove(parentheses) == 2
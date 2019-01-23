def is_well_formed(string):
    stack = [None]
    closed_dict = {")": "(", "}": "{", "]": "["}
    for bracket in string:
        if bracket in closed_dict:
            opened = closed_dict[bracket]
            if opened == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
    return len(stack) == 1

string = "([])[]({})"
assert is_well_formed(string) == True

string = "([)]"
assert is_well_formed(string) == False

string = "((()"
assert is_well_formed(string) == False

string = ")()("
assert is_well_formed(string) == False
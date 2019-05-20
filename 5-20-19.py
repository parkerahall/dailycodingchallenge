def first_recurring(string):
    output = None
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
        else:
            output = char
            break
    return output

string = "acbbac"
assert first_recurring(string) == "b"

string = "abcdef"
assert first_recurring(string) == None
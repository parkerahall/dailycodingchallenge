def encode(string):
    number = 0
    last_char = ""
    output = []
    for char in string:
        if char == last_char:
            number += 1
        else:
            output.append(str(number))
            output.append(last_char)

            number = 1
            last_char = char
    output.append(str(number))
    output.append(last_char)
    return "".join(output[2:])

def decode(code):
    output = []
    for i in range(0, len(code), 2):
        number = int(code[i])
        character = code[i + 1]
        output.append(character * number)
    return "".join(output)

string = "AAAABBBCCDAA"
assert decode(encode(string)) == string
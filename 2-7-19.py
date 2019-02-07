def line_break(string, k):
    words = string.split(" ")
    lines = [[]]
    current_length = 0
    for word in words:
        if len(word) > k:
            return None
        elif len(word) + current_length > k:
            lines.append([])
            current_length = 0

        lines[-1].append(word)
        current_length += len(word) + 1

    for i in range(len(lines)):
        lines[i] = " ".join(lines[i])
    return lines

string = "the quick brown fox jumps over the lazy dog"
k = 10
assert line_break(string, k) == ["the quick", "brown fox", "jumps over", "the lazy", "dog"]

string = "that dog is beautiful"
k = 7
assert line_break(string, k) == None
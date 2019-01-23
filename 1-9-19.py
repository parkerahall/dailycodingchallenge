def justify(words, k):
    lines_and_sizes = [[[], 0]]
    space_left = k
    for word in words:
        if len(word) <= space_left:
            lines_and_sizes[-1][0].append(word)
            lines_and_sizes[-1][1] += len(word)
            space_left -= (len(word) + 1)
        else:
            space_left = k - (len(word) + 1)
            lines_and_sizes.append([[word], len(word)])

    output = []
    for line, length in lines_and_sizes:
        empty_space = k - length
        string_list = []
        if len(line) > 1:
            per = empty_space / (len(line) - 1)
            extra = empty_space - per * (len(line) - 1)
            string_list = []
            for word in line:
                string_list.append(word)
                string_list.append(" " * (per + int(extra > 0)))
                extra -= 1
            string_list.pop()
        else:
            string_list.append(line[0])
            string_list.append(" " * empty_space)
        output.append("".join(string_list))
    return output
            

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
assert justify(words, k) == ["the  quick brown", "fox  jumps  over", "the   lazy   dog"]
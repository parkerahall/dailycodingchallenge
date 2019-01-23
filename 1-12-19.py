def edit_distance(first, second):
    first_len = len(first)
    second_len = len(second)

    cached = {}
    for i in range(first_len):
        cached[(i, second_len)] = first_len - i
    for j in range(second_len):
        cached[(first_len, j)] = second_len - j
    cached[(first_len, second_len)] = 0

    def edit_distance_dp(i, j):
        if (i, j) not in cached:
            sub_or_same = edit_distance_dp(i + 1, j + 1) + int(first[i] != second[j])
            insert_or_delete = 1 + min(edit_distance_dp(i + 1, j), edit_distance_dp(i, j + 1))
            cached[(i, j)] = min(sub_or_same, insert_or_delete)
        return cached[(i, j)]

    return edit_distance_dp(0, 0)

first = "kitten"
second = "sitting"
assert edit_distance(first, second) == 3

first = "kitten"
second = "kittens"
assert edit_distance(first, second) == 1

first = "backs"
second = "black"
assert edit_distance(first, second) == 2
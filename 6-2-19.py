def start_indices(s, words):
    word_length = len(words[0])

    valid_starts = []
    word_set = set(words)
    for i in range(len(s)):
        start_index = i
        curr_set = word_set.copy()
        while s[start_index : start_index + word_length] in curr_set:
            curr_set.remove(s[start_index : start_index + word_length])
            start_index += word_length
        if len(curr_set) == 0:
            valid_starts.append(i)

    return valid_starts

s = "dogcatcatcodecatdog"
words = ["cat", "dog"]
expected = [0, 13]
actual = start_indices(s, words)
assert set(expected) == set(actual)

s = "barfoobazbitbyte"
words = ["cat", "dog"]
expected = []
actual = start_indices(s, words)
assert set(expected) == set(actual)
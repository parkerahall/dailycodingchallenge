def is_palindrome(word):
    if len(word) < 2:
        return True

    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])

    return False

def palindrome_indices(words):
    output = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            for first, second in [(i, j), (j, i)]:
                if is_palindrome(words[first] + words[second]):
                    output.append((first, second))
    return output

words = ["code", "edoc", "da", "d"]
expected = [(0, 1), (1, 0), (2, 3)]
actual = palindrome_indices(words)
assert set(expected) == set(actual)
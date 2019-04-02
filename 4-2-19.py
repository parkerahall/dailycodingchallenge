from collections import defaultdict

def string_to_dict(string):
    freq = defaultdict(int)
    for letter in string:
        freq[letter] += 1
    return freq

def find_anagrams(string, word):
    word_len = len(word)
    word_dict = string_to_dict(word)

    string_len = len(string)

    return [i for i in range(string_len - word_len + 1) if string_to_dict(string[i : i + word_len]) == word_dict]

string = "abxaba"
word = "ab"
assert find_anagrams(string, word) == [0, 3, 4]
from collections import defaultdict

# O(N) runtime, where N = |string|
def string_to_dict(string):
    freq = defaultdict(int)
    for letter in string:
        freq[letter] += 1
    return freq

# O(NM) runtime, where N = |string| and M = |word|
def find_anagrams(string, word):
    word_len = len(word)
    word_dict = string_to_dict(word)

    string_len = len(string)

    return [i for i in range(string_len - word_len + 1) if string_to_dict(string[i : i + word_len]) == word_dict]

string = "abxaba"
word = "ab"
assert find_anagrams(string, word) == [0, 3, 4]

# using the assumption the string is in ASCII, we can achieve a faster runtime

# O(N) runtime, where N = max(|string|, |word|)
def find_anagrams_better(string, word):
    # 256 total possible characters in ASCII alphabet
    word_len = len(word)
    word_array = [0] * 256

    for letter in word:
        word_array[ord(letter)] += 1

    string_array = [0] * 256
    valid_starts = []
    for i in range(len(string)):
        if i >= word_len:
            string_array[ord(string[i - word_len])] -= 1

        string_array[ord(string[i])] += 1
        if string_array == word_array:
            valid_starts.append(i - word_len + 1)
    return valid_starts

string = "abxaba"
word = "ab"
assert find_anagrams_better(string, word) == [0, 3, 4]
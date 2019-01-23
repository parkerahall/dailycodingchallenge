from collections import defaultdict

# O(|dictionary|) runtime, but inefficient if same dictionary for every call
def autocomplete(s, dictionary):
    output = []
    pre_length = len(s)
    for word in dictionary:
        if word[:pre_length] == s:
            output.append(word)
    return output

# O(|dictionary| * |longest word|), but only needs to be called once
def precompute(dictionary):
    prefix_dict = defaultdict(list)
    for word in dictionary:
        for i in range(len(word)):
            prefix_dict[word[:i + 1]].append(word)
    return prefix_dict

# O(1) runtime
def autocomplete_pre(s, prefix_dict):
    return prefix_dict[s]

s = "de"
dictionary = ["dog", "deer", "deal"]
assert autocomplete(s, dictionary) == ["deer", "deal"]

prefix_dict = precompute(dictionary)
assert autocomplete_pre(s, prefix_dict) == ["deer", "deal"]
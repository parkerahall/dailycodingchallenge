def make_freq_dict(string):
    freq = {}
    for char in string:
        old = freq.get(char, 0)
        freq[char] = old + 1
    return freq

def make_freq_freq_dict(freq_dict):
    freq_freq = {}
    for char in freq_dict:
        freq = freq_dict[char]
        old = freq_freq.get(freq, 0)
        freq_freq[freq] = old + 1
    return freq_freq

def bijection_exists(s1, s2):
    return make_freq_freq_dict(make_freq_dict(s1)) == make_freq_freq_dict(make_freq_dict(s2))

s1 = "abc"
s2 = "bcd"
assert bijection_exists(s1, s2) == True

s1 = "foo"
s2 = "bar"
assert bijection_exists(s1, s2) == False

s1 = "hello"
s2 = "putt"
assert bijection_exists(s1, s2) == False
from collections import defaultdict

# O(|s|^2) runtime
def k_distinct_brute(s, k):
    max_length = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            seen.add(s[j])
            if len(seen) > k:
                max_length = max(max_length, j - i)
                break
    return max_length

def k_distinct(s, k):
    max_length = 0
    start = 0
    end = 0

    if len(s) == 0:
        return 0
    elif k >= len(s):
        return len(s)
    freq_dict = defaultdict(int)
    freq_dict[s[0]] += 1

    for _ in range(len(s) - 1):
        end += 1
        freq_dict[s[end]] += 1
        if len(freq_dict) > k:
            max_length = max(max_length, end - start)
            while len(freq_dict) > k:
                freq_dict[s[start]] -= 1
                if freq_dict[s[start]] == 0:
                    del freq_dict[s[start]]
                start += 1
    return max_length

s = "abcba"
k = 2
assert k_distinct(s, k) == 3

s = "aaaabbbbcccc"
k = 2
assert k_distinct(s, k) == 8

s = "ab"
k = 3
assert k_distinct(s, k) == 2
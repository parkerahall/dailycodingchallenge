def is_palindrome(string):
    start = 0
    end = len(string) - 1
    while start < end and string[start] == string[end]:
        start += 1
        end -= 1
    return start >= end

def palindrome_split(string):
    N = len(string)
    cached = {len(string) : []}

    def ps_dp(i):
        if i not in cached:
            best = list(string)
            for j in range(i, N):
                sub = string[i : j + 1]
                if is_palindrome(sub):
                    possible = [sub]
                    possible.extend(ps_dp(j + 1))
                    if len(possible) < len(best):
                        best = possible
            cached[i] = best
        return cached[i]

    return ps_dp(0)

string = "racecarannakayak"
expected = ["racecar", "anna", "kayak"]
actual = palindrome_split(string)
assert expected == actual

string = "abc"
expected = ["a", "b", "c"]
actual = palindrome_split(string)
assert expected == actual
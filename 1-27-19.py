# key format in cached : list of half palindrome if palindrome else None, palindrome code
# palindrome code : 0 -> even palindrome, 1 -> odd palindrome,
#                   2 -> old even palindrome, 3 -> old odd palindrome

EVEN = 0
ODD = 1
OLD_EVEN = 2
OLD_ODD = 3

PAL_TYPE_CONVERTER = { EVEN     : OLD_EVEN,
                  OLD_EVEN : OLD_EVEN,
                  ODD      : OLD_ODD,
                  OLD_ODD  : OLD_ODD }

def palindrome_length(pal_array, pal_type):
    return len(pal_array) - (pal_type % 2)

def longest_palindromic_substring(string):
    cached = {}
    for i in range(len(string)):
        cached[(i, i)] = ([string[i]], ODD)
        cached[(i + 1, i)] = [], EVEN

    def lps_dp(begin, end):
        if (begin, end) not in cached:
            inner_array, inner_pal_type = lps_dp(begin + 1, end - 1)
            right_array, right_pal_type = lps_dp(begin + 1, end)
            left_array, left_pal_type = lps_dp(begin, end - 1)

            inner_length = palindrome_length(inner_array, inner_pal_type)
            right_length = palindrome_length(right_array, right_pal_type)
            left_length = palindrome_length(left_array, left_pal_type)

            if inner_pal_type < OLD_EVEN and string[begin] == string[end]:
                inner_array.append(string[begin])
                cached[(begin, end)] = inner_array, inner_pal_type
            else:
                if inner_length >= right_length and inner_length >= left_length:
                    cached[(begin, end)] = inner_array, PAL_TYPE_CONVERTER[inner_pal_type]
                elif right_length >= inner_length and right_length >= left_length:
                    cached[(begin, end)] = right_array, PAL_TYPE_CONVERTER[right_pal_type]
                else:
                    cached[(begin, end)] = left_array, PAL_TYPE_CONVERTER[left_pal_type]
        
        return cached[(begin, end)]

    best_pal_array, best_pal_type = lps_dp(0, len(string) - 1)

    if best_pal_type % 2:
        return "".join(best_pal_array[::-1] + best_pal_array[1:])
    else:
        return "".join(best_pal_array[::-1] + best_pal_array)

string = "bananas"
assert longest_palindromic_substring(string) == "anana"

string = "airbnb"
assert longest_palindromic_substring(string) == "bnb"

string = "kayak"
assert longest_palindromic_substring(string) == "kayak"

string = "weather"
answer = longest_palindromic_substring(string)
assert answer in string
assert len(answer) == 1
def reverse_words(string):
    return (' ').join(string.split(' ')[::-1])

string = "hello world here"
expected = "here world hello"
assert reverse_words(string) == expected

def reverse(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

def reverse_words_in_place(string_list):
    string_len = len(string_list)
    reverse(string_list, 0, string_len - 1)

    start = 0
    end = 0
    while end < string_len:
        if string_list[end] == " ":
            reverse(string_list, start, end - 1)
            start = end + 1
        end += 1
    reverse(string_list, start, end - 1)

    return string_list

string = list("hello world here")
expected = list("here world hello")
assert reverse_words_in_place(string) == expected
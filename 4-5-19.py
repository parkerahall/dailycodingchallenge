def reverse_words_with_delimiters(string, delimiters):
    word_array = []
    delim_array = []
    
    start = 0
    while start < len(string) and string[start] in delimiters:
        start += 1
    delim_array.append(string[:start])

    end = len(string) - 1
    while end >= 0 and string[end] in delimiters:
        end -= 1
    last_delim = string[end + 1:]

    last_start = start
    delim_chunk = False
    while start < end:
        if (string[start] in delimiters) ^ delim_chunk:
            current_chunk = string[last_start:start]
            if delim_chunk:
                delim_array.append(current_chunk)
            else:
                word_array.append(current_chunk)
            last_start = start
            delim_chunk = not delim_chunk
        start += 1
    
    last_chunk = string[last_start:end + 1]
    if string[start - 1] in delimiters:
        delim_array.append(last_chunk)
    else:
        word_array.append(last_chunk)

    total_array = []
    word_array_len = len(word_array)
    for i in range(len(delim_array) + len(word_array)):
        if i % 2:
            total_array.append(word_array[word_array_len - i / 2 - 1])
        else:
            total_array.append(delim_array[i / 2])
    total_array.append(last_delim)
    
    return ''.join(total_array)


string = "hello/world:here"
delimiters = set(["/", ":"])
expected = "here/world:hello"
assert reverse_words_with_delimiters(string, delimiters) == expected

string = "hello/world:here/"
delimiters = set(["/", ":"])
expected = "here/world:hello/"
assert reverse_words_with_delimiters(string, delimiters) == expected

string = "hello//world:here"
delimiters = set(["/", ":"])
expected = "here//world:hello"
assert reverse_words_with_delimiters(string, delimiters) == expected
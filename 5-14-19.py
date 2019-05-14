def smallest_distance(string, first, second):
    swap_dict = {first : second, second : first, None : None}
    
    words = string.split(' ')
    best = len(words)
    dist = 0
    last = None
    for word in words:
        if last == None and word in swap_dict:
            last = word
        elif word == last:
            dist = 0
        elif swap_dict[last] == word:
            best = min(best, dist)
            dist = 0
            last = word
        elif last != None:
            dist += 1
    return best

string = "dog cat hello cat dog dog hello cat world"

first = "hello"
second = "world"
assert smallest_distance(string, first, second) == 1
assert smallest_distance(string, second, first) == 1

first = "dog"
second = "cat"
assert smallest_distance(string, first, second) == 0
assert smallest_distance(string, second, first) == 0

first = "world"
second = "dog"
assert smallest_distance(string, first, second) == 2
assert smallest_distance(string, second, first) == 2
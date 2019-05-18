import random

def find_majority(lst):
    last = None
    count = 0
    for elt in lst:
        if count == 0:
            last = elt
            count += 1
        elif elt == last:
            count += 1
        else:
            count -= 1
    return last

N = 100
lst = [1, 1, 1, 1, 1, 2, 3, 4, 5]
for _ in range(N):
    random.shuffle(lst)
    assert find_majority(lst) == 1
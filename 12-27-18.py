from random import random
from collections import defaultdict

def pick_random(stream):
    num_seen = 0
    chosen_elt = None
    for element in stream:
        num_seen += 1
        bound = 1. / num_seen
        if random() <= bound:
            chosen_elt = element
    return chosen_elt

stream = [1, 2, 3, 4, 5]
freq_dict = defaultdict(int)
for _ in range(1000):
    freq_dict[pick_random(stream)] += 1
print freq_dict
import random
from collections import defaultdict

def rand_k(k):
    return random.randint(1, k)

def shuffle(cards):
    num_cards = len(cards)
    for set_index in range(num_cards):
        # minus 1 to make it zero indexed
        swap_index = rand_k(num_cards - set_index) - 1 + set_index
        cards[set_index], cards[swap_index] = cards[swap_index], cards[set_index]
    return cards

cards = [1, 2, 3, 4, 5]
freq_dict = defaultdict(int)
for _ in range(10000):
    shuffle(cards)
    freq_dict[tuple(cards)] += 1

print max(freq_dict.values())
print min(freq_dict.values())
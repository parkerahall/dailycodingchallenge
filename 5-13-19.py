import random
from collections import defaultdict

def random_sample(numbers, probs):
    seed = random.random()
    i = 0
    while seed >= probs[i]:
        seed -= probs[i]
        i += 1
    return numbers[i]

numbers = [1, 2, 3, 4]
probs = [.1, .5, .2, .2]
freq = defaultdict(float)
N = 10000
for _ in range(N):
    freq[random_sample(numbers, probs)] += (1. / N)
print(freq)
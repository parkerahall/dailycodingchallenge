import random

BIAS = random.random()
while BIAS == 0:
    BIAS = random.random()

def toss_biased():
    return int(random.random() < BIAS)

def toss_unbiased():
    first = toss_biased()
    second = toss_biased()
    while first == second:
        first = toss_biased()
        second = toss_biased()
    return first

N = 10000
total = 0.
for _ in range(N):
    total += toss_unbiased()
print total / N
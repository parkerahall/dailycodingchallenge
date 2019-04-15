import random
from math import log

def expected_rounds(n):
    return log(n, 2)

def run_once(n):
    current = n
    num_rounds = 0
    while current > 1:
        new = 0
        for _ in range(current):
            if random.random() < .5:
                new += 1
        current = new
        num_rounds += 1
    return num_rounds

def expected_rounds_est(n, num_trials=10000):
    total = 0.
    for _ in range(num_trials):
        total += run_once(n)
    return total / num_trials

for i in range(100):
    n = (i + 1) * 10
    print(expected_rounds(n), expected_rounds_est(n))
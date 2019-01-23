from random import random

def pi_est(r):
    quarter = 0
    for x in range(r):
        y = (r ** 2 - x ** 2) ** .5
        quarter += y
    area = quarter * 4
    return area / (r ** 2)

def pi_est_mc(r, n):
    hits = 0.
    for _ in range(n):
        rand_x = random() * r
        rand_y = random() * r
        hits += (rand_x ** 2) + (rand_y ** 2) <= r ** 2
    return hits / n * 4

print pi_est_mc(5, 10000)
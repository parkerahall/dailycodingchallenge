from collections import defaultdict

def bishop_attacks(bishops):
    sum_dict = defaultdict(int)
    diff_dict = defaultdict(int)
    for row, col in bishops:
        sum_dict[row + col] += 1
        diff_dict[row - col] += 1
    
    total = 0
    for key in sum_dict:
        n = sum_dict[key]
        total += (n * (n - 1) / 2.)
    for key in diff_dict:
        n = diff_dict[key]
        total += (n * (n - 1) / 2.)
    return total

bishops = [(0, 0), (1, 2), (2, 2), (4, 0)]
assert bishop_attacks(bishops) == 2

bishops = [(0, 0), (1, 2), (2, 2), (4, 0), (1, 1), (3, 3), (2, 4), (4, 2)]
assert bishop_attacks(bishops) == 10
import random
from collections import defaultdict

def rand5():
    return random.randint(1, 5)

def rand7():
    conversion = {}
    num = 0
    for first_pick in range(1, 6):
        for second_pick in range(1, 6):
            if num >= 21:
                break
            conversion[(first_pick, second_pick)] = (num % 7) + 1
            num += 1

    first_pick = rand5()
    second_pick = rand5()
    while (first_pick, second_pick) not in conversion:
        first_pick = rand5()
        second_pick = rand5()
    return conversion[(first_pick, second_pick)]

values = defaultdict(int)
for _ in range(1000):
    values[rand7()] += 1
print values
import random

def runout(N, goal):
    ev = 0.
    last = len(goal)
    for _ in range(N):
        rolls = []
        while rolls[-last:] != goal:
            rolls.append(random.randint(1, 6))
        ev += len(rolls)
    return ev / N

def expected_club_dues(N):
    five_six_ev = runout(N, [5, 6])
    five_five_ev = runout(N, [5, 5])
    print("Expected club dues for 5-6: " + str(five_six_ev))
    print("Expected club dues for 5-5: " + str(five_five_ev))

N = 10000
expected_club_dues(N)
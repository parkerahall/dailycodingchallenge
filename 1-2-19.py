def intersect(int1, int2):
    start_1, end_1 = int1
    start_2, end_2 = int2
    return end_2 > start_1 and end_1 > start_2

def num_classrooms_brute(intervals):
    output = 0
    current_schedule = []
    interval_set = set(intervals)
    while len(interval_set) > 0:
        interval = interval_set.pop()
        current_schedule.append(interval)
        to_remove = []
        for elt in interval_set:
            add = True
            for placed in current_schedule:
                if intersect(elt, placed):
                    add = False
                    break
            if add:
                current_schedule.append(elt)
                to_remove.append(elt)
        for elt in to_remove:
            interval_set.remove(elt)
        output += 1
        current_schedule = []
    return output

def num_classrooms(intervals):
    starts = set()
    ends = set()
    all_times = []
    for start, end in intervals:
        starts.add(start)
        ends.add(end)
        all_times.extend([start, end])

    all_times.sort()
    num_classrooms = 0
    maximum = 0
    for time in all_times:
        if time in starts:
            num_classrooms += 1
        if time in ends:
            num_classrooms -= 1
        maximum = max(maximum, num_classrooms)
    return maximum

intervals = [(30, 75), (0, 50), (60, 150)]
assert num_classrooms_brute(intervals) == 2

intervals = [(30, 75), (0, 50), (60, 150)]
assert num_classrooms(intervals) == 2
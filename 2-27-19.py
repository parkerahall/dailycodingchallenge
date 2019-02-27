def combine_intervals(intervals):
    if len(intervals) == 0:
        return []

    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    output = [sorted_intervals[0]]
    for i in range(1, len(sorted_intervals)):
        curr_start, curr_end = sorted_intervals[i]
        last_start, last_end = output[-1]

        if curr_start < last_end:
            output[-1] = (last_start, max(last_end, curr_end))
        else:
            output.append((curr_start, curr_end))
    return output

intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
assert combine_intervals(intervals) == [(1, 3), (4, 10), (20, 25)]

intervals = [(5, 8), (1, 3), (20, 25), (4, 10)]
assert combine_intervals(intervals) == [(1, 3), (4, 10), (20, 25)]
def in_interval(interval, number):
    return number >= interval[0] and number <= interval[1]

def check_answer(intervals, answer):
    filled = set()
    for number in answer:
        for i in range(len(intervals)):
            if in_interval(intervals[i], number):
                filled.add(i)
    return len(filled) == len(intervals)

def minimum_interval_cover_brute(intervals):
    if len(intervals) == 0:
        return set()
    
    start, end = intervals[0]
    best_length = len(intervals) - 1
    best_cover = None
    for guess in range(start, end + 1):
        new_intervals = []
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if not in_interval(curr, guess):
                new_intervals.append(curr)
        smaller_cover = minimum_interval_cover_brute(new_intervals)
        if len(smaller_cover) <= best_length:
            smaller_cover.add(guess)
            best_length = len(smaller_cover)
            best_cover = smaller_cover
    return best_cover

def minimum_interval_cover(intervals):
    if len(intervals) == 0:
        return set()

    end = min([end for (start, end) in intervals])
    new_intervals = [interval for interval in intervals if not in_interval(interval, end)]
    ans = minimum_interval_cover(new_intervals)
    ans.add(end)
    return ans

intervals = [[0, 3], [2, 6], [3, 4], [6, 9]]
answer = set([3, 6])
assert check_answer(intervals, answer) == True

intervals = [[0, 3], [2, 6], [3, 4], [6, 9]]
answer = minimum_interval_cover_brute(intervals)
assert check_answer(intervals, answer) == True
assert len(answer) == 2

intervals = [[0, 3], [2, 6], [3, 4], [6, 9]]
answer = minimum_interval_cover(intervals)
assert check_answer(intervals, answer) == True
assert len(answer) == 2
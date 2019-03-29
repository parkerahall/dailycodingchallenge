# can only move array[i] hops
def reach_end_strict(array):
    curr_index = 0
    while curr_index < len(array) - 1:
        if array[curr_index] == 0:
            return False
        curr_index += array[curr_index]
    return curr_index == len(array) - 1

array = [2, 0, 1, 0]
assert reach_end_strict(array) == True

array = [1, 1, 0, 1]
assert reach_end_strict(array) == False

array = [2, 2, 0, 0]
assert reach_end_strict(array) == False

# can move 1 to array[i] hops
def reach_end(array):
    cached = {}

    def reach_end_dp(i):
        if i not in cached:
            if i == len(array) - 1:
                cached[i] = True
            elif i >= len(array):
                cached[i] = False
            else:
                hops = array[i]
                can_reach = False
                for hop in range(1, hops + 1):
                    can_reach = can_reach or reach_end_dp(i + hop)
                cached[i] = can_reach
        return cached[i]

    return reach_end_dp(0)

array = [2, 0, 1, 0]
assert reach_end(array) == True

array = [1, 1, 0, 1]
assert reach_end(array) == False

array = [2, 2, 0, 0]
assert reach_end(array) == True
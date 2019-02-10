def partition(elements):
    num_elements = len(elements)
    cached = {}

    def partition_dp(i, diff):
        if (i, diff) not in cached:
            if i >= num_elements:
                cached[(i, diff)] = diff == 0
            else:
                add_to_left = partition_dp(i + 1, diff + elements[i])
                add_to_right = partition_dp(i + 1, diff - elements[i])
                valid = add_to_left or add_to_right
                cached[(i, diff)] = valid
        return cached[(i, diff)]

    return partition_dp(0, 0)

elements = [15, 5, 20, 10, 35, 15, 10]
assert partition(elements) == True

elements = [15, 5, 20, 10, 35]
assert partition(elements) == False
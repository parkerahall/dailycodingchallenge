def target_subset(integers, target):
    cached = {}
    list_length = len(integers)
    for i in range(1, target + 1):
        cached[(list_length, i)] = None

    for i in range(list_length + 1):
        cached[(i, 0)] = []

    def target_subset_dp(index, sub_target):
        if (index, sub_target) not in cached:
            current_num = integers[index]
            without_current = target_subset_dp(index + 1, sub_target)
            
            if without_current == None and current_num <= sub_target:
                with_current = target_subset_dp(index + 1, sub_target - current_num)
                if with_current != None:
                    with_current.append(current_num)
                cached[(index, sub_target)] = with_current
            else:
                cached[(index, sub_target)] = without_current

        return cached[(index, sub_target)]

    return target_subset_dp(0, target)

integers = [12, 1, 61, 5, 9, 2]
target = 24
assert sorted(target_subset(integers, target)) == [1, 2, 9, 12]

integers = [12, 1, 61, 5, 2]
target = 24
assert target_subset(integers, target) == None
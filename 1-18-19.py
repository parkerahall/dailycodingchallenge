def power_set(input_set, previous=[]):
    if len(previous) == 0:
        previous.append(set())
    if len(input_set) == 0:
        return previous

    next_elt = input_set.pop()
    new_previous = []
    for prev_set in previous:
        new_previous.append(prev_set)
        cpy = prev_set.copy()
        cpy.add(next_elt)
        new_previous.append(cpy)
    return power_set(input_set, new_previous)

input_set = set([1, 2, 3])
correct = [set(), set([1]), set([2]), set([3]), set([1, 2]), set([2, 3]), set([1, 3]), set([1, 2, 3])]
answer = power_set(input_set)
for s in answer:
    assert s in correct
assert len(answer) == len(correct)

def power_set_generator(input_list, index, prev_set):
    if index >= len(input_list):
        yield prev_set
    else:
        for elt in power_set_generator(input_list, index + 1, prev_set):
            yield elt
        prev_set.add(input_list[index])
        for elt in power_set_generator(input_list, index + 1, prev_set):
            yield elt

input_list = [1, 2, 3]
length = 0
correct = [set(), set([1]), set([2]), set([3]), set([1, 2]), set([2, 3]), set([1, 3]), set([1, 2, 3])]
answer = power_set_generator(input_list, 0, set())
length = 0
for s in answer:
    length += 1
    assert s in correct
assert length == len(correct)
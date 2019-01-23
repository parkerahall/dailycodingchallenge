def smallest_missing_positive(l):
    num_elts = len(l)
    num_negative = 0
    scan_index = 0
    
    while scan_index < num_elts - num_negative:
        if l[scan_index] < 1:
            num_negative += 1
            l[scan_index], l[num_elts - num_negative] = l[num_elts - num_negative], l[scan_index]
        else:
            scan_index += 1

    pos_elts = l[:num_elts - num_negative]
    num_positive = num_elts - num_negative
    for i in range(num_positive):
        val = abs(pos_elts[i])
        if val <= num_positive:
            if pos_elts[val - 1] > 0:
                pos_elts[val - 1] *= -1

    for j in range(num_positive):
        if pos_elts[j] > 0:
            return j + 1
    
    return num_positive + 1


l = [3, 4, -1, 1, -1]
assert smallest_missing_positive(l) == 2

l = [1, 2, 0]
assert smallest_missing_positive(l) == 3

l = [0, -1, -3, 0]
assert smallest_missing_positive(l) == 1

l = [3, 4, -1, 1, 1, 4, 3 -6, 0]
assert smallest_missing_positive(l) == 2
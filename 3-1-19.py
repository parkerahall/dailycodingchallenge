def get(array, index, default):
    if index < 0 or index >= len(array):
        return default
    return array[index]

def one_away_nondecreasing(array):
    if len(array) == 0:
        return True

    total = 0
    current = array[0]
    for elem in array:
        if elem < current:
            total += 1
        current = elem
    return total <= 1

array = [10, 5, 7]
assert one_away_nondecreasing(array) == True

array = [10, 5, 1]
assert one_away_nondecreasing(array) == False
# can be solved in O(nlogn) time with balanced BST, but I don't want to implement a balanced BST
def num_smaller_after(array):
    output = [0] * len(array)
    for i in range(len(array)):
        number = array[i]
        for j in range(i + 1, len(array)):
            if array[j] < number:
                output[i] += 1
    return output

array = [3, 4, 9, 6, 1]
expected = [1, 1, 2, 1, 0]
assert num_smaller_after(array) == expected
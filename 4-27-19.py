def find_max(row):
    largest = 0

    current = 0
    for col in row:
        if col:
            current += col
        else:
            largest = max(largest, current)
            current = 0
    largest = max(largest, current)
    return largest

def largest_rectangle(matrix):
    largest = find_max(matrix[0])

    for i in range(1, len(matrix)):
        last_row = matrix[i - 1]
        curr_row = matrix[i]
        for j in range(len(curr_row)):
            if curr_row[j]:
                curr_row[j] += last_row[j]
        largest = max(largest, find_max(curr_row))

    return largest


matrix = [[1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [0, 1, 0, 0]]
assert largest_rectangle(matrix) == 4
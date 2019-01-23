from collections import deque

def k_max_brute(array, k):
    if len(array) > 0:
        largest = array[0]
        for i in range(len(array) - k + 1):
            print max(array[i: i + k])

def k_max(array, k):
    d = deque()

    for i in range(k):
        while len(d) > 0 and array[i] >= array[d[-1]]:
            d.pop()

        d.append(i)

    for j in range(k, len(array)):
        print array[d[0]]

        while len(d) > 0 and d[0] <= j - k:
            d.popleft()

        while len(d) and array[j] >= array[d[-1]]:
            d.pop()

        d.append(j)

    print array[d[0]]

array = [10, 5, 2, 7, 8, 7]
k = 3
k_max(array, k)
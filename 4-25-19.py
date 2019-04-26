class SparseArray:
    def __init__(self, arr):
        self.nonzero = {}
        
        for i in range(len(arr)):
            if arr[i] != 0:
                self.nonzero[i] = arr[i]

    def set(self, i, val):
        if i in self.nonzero and val == 0:
            del self.nonzero[i]
        elif val != 0:
            self.nonzero[i] = val

    def get(self, i):
        return self.nonzero.get(i, 0)

big_array = [0] * 1000
indices = [0, 250, 333, 750]
values = [1, 2, 7, 21]
for i in range(len(indices)):
    big_array[indices[i]] = values[i]
sparse = SparseArray(big_array)

for i in range(1000):
    value = 0 if i not in indices else values[indices.index(i)]
    assert sparse.get(i) == value

sparse.set(300, 1000)
assert sparse.get(300) == 1000
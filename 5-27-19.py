class TwoDIterator:
    def __init__(self, arrs):
        self.arrays = arrs
        self.outer_index = 0
        self.inner_index = 0

    def next(self):
        if self.has_next():
            value = self.arrays[self.outer_index][self.inner_index]
            self.inner_index += 1

            while self.has_next() and self.inner_index == len(self.arrays[self.outer_index]):
                self.inner_index = 0
                self.outer_index += 1

            return value
        else:
            raise StopIteration

    def has_next(self):
        return self.outer_index < len(self.arrays)

arrs = [[1, 2], [3], [], [4, 5, 6]]
itr = TwoDIterator(arrs)
while itr.has_next():
    print(itr.next())
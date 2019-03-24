# O(n) time for get and set because I don't want to implement a self-balancing binary tree
class Map:
    def __init__(self):
        self.times = {}
        self.values = {}

    def set(self, key, value, time):
        if key not in self.times:
            self.times[key] = []
            self.values[key] = []

        if time in self.times[key]:
            index = self.times[key].index(time)
            self.values[key][index] = value
        else:
            index = 0
            while index < len(self.times[key]) and self.times[key][index] < time:
                index += 1

            self.times[key].insert(index, time)
            self.values[key].insert(index, value)

    def get(self, key, time):
        if key not in self.times:
            raise KeyError

        if time < self.times[key][0]:
            return None

        index = 0
        while index < len(self.times[key]) and self.times[key][index] <= time:
            index += 1

        return self.values[key][index - 1]

d = Map()
d.set(1, 1, 0)
d.set(1, 2, 2)
assert d.get(1, 1) == 1
assert d.get(1, 3) == 2

d.set(2, 1, 5)
assert d.get(2, 0) == None
assert d.get(2, 10) == 1

d.set(3, 1, 0)
d.set(3, 2, 0)
assert d.get(3, 0) == 2
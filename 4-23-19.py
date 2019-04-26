class HitCounter:
    def __init__(self):
        self.total_hits = 0
        self.hits = []
    
    def record(self, timestamp):
        if len(self.hits) == 0:
            self.hits.append((timestamp, 1))
        else:
            last_timestamp, amount = self.hits[-1]
            if timestamp == last_timestamp:
                self.hits[-1] = (last_timestamp, amount + 1)
            else:
                self.hits.append((timestamp, 1))
        self.total_hits += 1

    def total(self):
        return self.total_hits

    def range(self, lower, upper):
        total = 0
        for time, amount in self.hits:
            if time >= lower and time <= upper:
                total += amount
        return total

counter = HitCounter()
hits = [(0, 5), (1, 4), (2, 1), (10, 5)]
for time, clicks in hits:
    for _ in range(clicks):
        counter.record(time)

assert counter.total() == 15
assert counter.range(-1, 11) == 15
assert counter.range(0, 10) == 15
assert counter.range(1, 5) == 5
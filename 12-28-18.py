class Log:
    def __init__(self, N):
        self.N = N
        self.length = 0
        self.log = [None] * self.N

    def record(self, order_id):
        self.log[(self.length % self.N)] = order_id
        self.length += 1

    def get_last(self, i):
        if self.length >= self.N:
            start = self.length - self.N
        else:
            start = 0
        return self.log[(start + i - 1) % self.N]

log = Log(3)
log.record(1)
log.record(2)
assert log.get_last(1) == 1
assert log.get_last(2) == 2
log.record(3)
assert log.get_last(1) == 1
log.record(4)
assert log.get_last(1) == 2
assert log.get_last(2) == 3
assert log.get_last(3) == 4
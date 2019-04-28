class BitArray:
    def __init__(self, size):
        self.bits = [0] * size

    def set(self, i, val):
        self.bits[i] = val

    def get(self, i):
        return self.bits[i]
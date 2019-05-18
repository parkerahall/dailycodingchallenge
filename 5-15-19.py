import random

class MaxHeap:
    def __init__(self, f):
        self.heap = []
        self.key_func = f

    def push(self, item):
        index = len(self.heap)
        self.heap.append(item)
        self.trickle_up(index)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self.trickle_down(0)
        return item

    def trickle_up(self, index):
        if index > 0:
            parent = (index + 1) / 2 - 1
            if self.key_func(self.heap[index]) > self.key_func(self.heap[parent]):
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self.trickle_up(parent)

    def trickle_down(self, index):
        left = (index + 1) * 2 - 1
        right = left + 1

        if left < len(self.heap):
            best_index = left
            best_key = self.key_func(self.heap[left])

            if right < len(self.heap):
                right_key = self.key_func(self.heap[right])
                if right_key > best_key:
                    best_index = right
                    best_key = right_key

            if best_key > self.key_func(self.heap[index]):
                self.heap[index], self.heap[best_index] = self.heap[best_index], self.heap[index]
                self.trickle_down(best_index)

    def size(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

class Stack:
    def __init__(self):
        self.heap = MaxHeap(lambda x: x[1])

    def push(self, item):
        key = self.heap.size()
        item = (item, key)
        self.heap.push(item)

    def pop(self):
        return self.heap.pop()[0]

N = 100
stack = Stack()
elements = []
for _ in range(N):
    item = random.random() * N
    elements.append(item)
    stack.push(item)

for _ in range(N):
    expected = elements.pop()
    actual = stack.pop()
    assert expected == actual


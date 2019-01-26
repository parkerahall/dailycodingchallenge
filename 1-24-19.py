class Stack:
    def __init__(self):
        self.elements = []
        self.maxes = []

    def push(self, val):
        self.elements.append(val)
        if len(self.maxes) == 0 or val >= self.maxes[-1]:
            self.maxes.append(val)

    def pop(self):
        last_elt = self.elements.pop()
        if last_elt == self.maxes[-1]:
            self.maxes.pop()
        return last_elt

    def max(self):
        return self.maxes[-1]

stack = Stack()
for i in range(5):
    stack.push(i)

for i in range(5):
    assert stack.max() == (5 - i - 1)
    assert stack.pop() == (5 - i - 1)

stack = Stack()
for j in range(5):
    stack.push(5 - j)

for j in range(5):
    assert stack.max() == 5
    assert stack.pop() == (j + 1)
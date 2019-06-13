class Stack:
    def __init__(self):
        self.elements = []

    @classmethod
    def from_list(cls, lst):
        s = Stack()
        s.elements = lst
        return s

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def length(self):
        return len(self.elements)

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False
        return self.elements == other.elements

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        return self.elements.pop(0)

    def length(self):
        return len(self.elements)

def split_reverse_merge_in_place(stack):
    N = stack.length()
    queue = Queue()

    for i in range(N - 1, 1, -1):
        for _ in range(i):
            queue.enqueue(stack.pop())
        for _ in range(i):
            stack.push(queue.dequeue())

stack = Stack.from_list([1, 2, 3, 4, 5])
expected = Stack.from_list([1, 5, 2, 4, 3])
split_reverse_merge_in_place(stack)
assert stack == expected

stack = Stack.from_list([1, 2, 3, 4])
expected = Stack.from_list([1, 4, 2, 3])
split_reverse_merge_in_place(stack)
assert stack == expected
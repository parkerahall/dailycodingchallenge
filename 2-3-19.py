class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, elt):
        self.elements.append(elt)

    def pop(self):
        return self.elements.pop()

class Queue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, elt):
        self.enqueue_stack.push(elt)

    def dequeue(self):
        if self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                new_elt = self.enqueue_stack.pop()
                self.dequeue_stack.push(new_elt)
        return self.dequeue_stack.pop()

queue = Queue()
for i in range(100):
    queue.enqueue(i)

for i in range(100):
    assert queue.dequeue() == i
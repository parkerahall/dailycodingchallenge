import random

NUM_STACKS = 3

class Stack:
    def __init__(self):
        self.list = []
        self.stack_lengths = [0] * NUM_STACKS

    def pop(self, stack_number):
        if self.stack_lengths[stack_number] == 0:
            raise IndexError("pop from empty stack")

        new_length = self.stack_lengths[stack_number] - 1
        index = new_length * NUM_STACKS + stack_number
        value = self.list[index]
        self.list[index] = None
        self.stack_lengths[stack_number] = new_length

        return value

    def push(self, item, stack_number):
        new_length = self.stack_lengths[stack_number] + 1
        while len(self.list) < new_length * NUM_STACKS:
            self.list.extend([None] * NUM_STACKS)

        index = self.stack_lengths[stack_number] * NUM_STACKS + stack_number
        self.list[index] = item
        self.stack_lengths[stack_number] = new_length

N = 50
stack = Stack()
push_calls = []
stack_values = [[] for _ in range(NUM_STACKS)]
for _ in range(N):
    stack_number = random.randrange(0, NUM_STACKS)
    value = random.random()
    push_calls.append((stack_number, value))
    stack_values[stack_number].append(value)

for i in range(N):
    stack_number, value = push_calls[i]
    stack.push(value, stack_number)

for j in range(N):
    stack_number, _ = push_calls[j]
    expected_value = stack_values[stack_number].pop()
    assert stack.pop(stack_number) == expected_value

for k in range(NUM_STACKS):
    try:
        stack.pop(k)
        assert False
    except IndexError:
        assert True
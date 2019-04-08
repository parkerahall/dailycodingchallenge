import random
from node import Node

def generate():
    left = None
    right = None
    if random.random() < .5:
        left = generate()
        right = generate()
    return Node(random.randint(1, 10), left=left, right=right)

for _ in range(10):
    root = generate()
    root.print_levels()
    print("NEXT")

class LazyNode:
    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None

        self.left_set = False
        self.right_set = False

    @property
    def left(self):
        if not self.left_set:
            if random.random() < .5:
                left_child = LazyNode(0)
                self._left = left_child
                left_child.parent = self
            self.left_set = True
        return self._left

    @property
    def right(self):
        if not self.right_set:
            if random.random() < .5:
                right_child = LazyNode(0)
                self._right = right_child
                right_child.parent = self
            self.right_set = True
        return self._right

def generate_lazy():
    return LazyNode(0)
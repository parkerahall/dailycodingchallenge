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
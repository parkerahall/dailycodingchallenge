class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def second_largest(root):
    current = root
    while current.right is not None:
        current = current.right
    if current.left is not None:
        current = current.left
        while current.right is not None:
            current = current.right
    else:
        current = current.parent
    return current

root = Node(1)

left = Node(2)
right = Node(3)

rr = Node(4)

rrl = Node(3.5)

rrll = Node(3.4)
rrlr = Node(3.6)

rrlrr = Node(3.7)

root.left = left
root.right = right
left.parent = root
right.parent = root

right.right = rr
rr.parent = right

assert second_largest(root).value == 3

rr.left = rrl
rrl.parent = rr

assert second_largest(root).value == 3.5

rrl.left = rrll
rrl.right = rrlr
rrll.parent = rrl
rrlr.parent = rrl

rrl.right = rrlrr
rrlrr.parent = rrl

assert second_largest(root).value == 3.7
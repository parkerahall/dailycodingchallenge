from node import Node

def next_largest(node):
    if node.right != None:
        current = node.right
        while current.left != None:
            current = current.left
        return current.value
    
    current = node
    while current.parent != None and current == current.parent.right:
        current = current.parent
    
    if current.parent == None:
        return None
    return current.parent.value

root = Node(10)
left = Node(5)
right = Node(30)
rl = Node(22)
rr = Node(35)

root.left = left
left.parent = root
assert next_largest(root) == None

root.right = right
right.parent = root
right.left = rl
rl.parent = right
assert next_largest(rl) == 30

right.right = rr
rr.parent = right
assert next_largest(rr) == None
assert next_largest(root) == 22
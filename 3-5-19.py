from node import Node

def print_tree(root):
    frontier = [root]
    while len(frontier) != 0:
        print([node.value for node in frontier])
        new_frontier = []
        for node in frontier:
            if node.left != None:
                new_frontier.append(node.left)
            if node.right != None:
                new_frontier.append(node.right)
        frontier = new_frontier

def invert(root):
    if root != None:
        root.left, root.right = root.right, root.left
        invert(root.left)
        invert(root.right)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.parent = a
c.parent = a

b.left = d
b.right = e
d.parent = b
e.parent = b

c.left = f
f.parent = c

print_tree(a)
invert(a)
print_tree(a)
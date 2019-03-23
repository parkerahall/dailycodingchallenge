from node import Node

def BST_min_max_size(root):
    minimum = root.value
    maximum = root.value

    is_BST = True
    size = 1
    best_BST = root
    best_BST_size = size
    
    if root.left != None:
        left_best, left_size, left_min, left_max = BST_min_max_size(root.left)
        minimum = left_min

        if left_size > best_BST_size:
            best_BST_size = left_size
            best_BST = left_best
        
        if left_best == root.left and left_max < root.value:
            size += left_size
        else:
            is_BST = False

    if root.right != None:
        right_best, right_size, right_min, right_max = BST_min_max_size(root.right)
        maximum = right_max
        
        if right_size > best_BST_size:
            best_BST_size = right_size
            best_BST = right_best
        
        if right_best == root.right and right_min >= root.value:
            size += right_size
        else:
            is_BST = False

    if is_BST and size > best_BST_size:
        best_BST_size = size
        best_BST = root

    return best_BST, best_BST_size, minimum, maximum

def largest_BST(root):
    best_BST, best_size, _, _ = BST_min_max_size(root)
    return best_BST, best_size

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

b.right = d
b.left = a
a.parent = b
d.parent = b

d.left = c
c.parent = d

assert largest_BST(b) == (b, 4)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

c.right = d
c.left = a
d.parent = c
a.parent = c

d.left = b
b.parent = d

assert largest_BST(c) == (d, 2)
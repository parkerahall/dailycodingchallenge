from node import Node

def is_valid(root):
    
    def is_valid_recurs(root):
        minimum = root.value
        maximum = root.value
        if root.left != None:
            valid_check = is_valid_recurs(root.left)
            if not valid_check:
                return False
            left_min, left_max = valid_check
            if left_max > root.value:
                return False
            minimum = min(minimum, left_min)
        if root.right != None:
            valid_check = is_valid_recurs(root.right)
            if not valid_check:
                return False
            right_min, right_max = valid_check
            if right_min < root.value:
                return False
            maximum = max(maximum, right_max)
        return minimum, maximum

    return is_valid_recurs(root) != False

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

assert is_valid(b) == True

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

assert is_valid(c) == False
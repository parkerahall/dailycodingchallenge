from node import Node

def minimum_level_sum(root):
    min_level = 0
    min_sum = root.value
    current = [root]
    curr_level = 0
    while len(current) > 0:
        curr_sum = 0
        new_current = []
        for elt in current:
            curr_sum += elt.value
            if elt.left != None:
                new_current.append(elt.left)
            if elt.right != None:
                new_current.append(elt.right)
        if curr_sum < min_sum:
            min_sum = curr_sum
            min_level = curr_level
        current = new_current
        curr_level += 1
    return min_level

root = Node(1, left=Node(2), right=Node(3))
assert minimum_level_sum(root) == 0

root = Node(10, left=Node(3), right=Node(6, left=Node(12), right=Node(0)))
assert minimum_level_sum(root) == 1
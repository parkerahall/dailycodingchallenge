from node import Node

def minimum_path_sum(root):
    if root == None:
        return 0

    left = minimum_path_sum(root.left)
    right = minimum_path_sum(root.right)
    return min(left, right) + root.value

root = Node(10, left=Node(5, right=Node(2)), right=Node(5, right=Node(1, left=Node(-1))))
assert minimum_path_sum(root) == 15
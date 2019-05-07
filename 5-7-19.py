from node import Node

def is_all_zeros(root):
    if root == None:
        return True
    return root.value == 0 and is_all_zeros(root.left) and is_all_zeros(root.right)

def prune(root):
    if is_all_zeros(root):
        return None

    if is_all_zeros(root.left):
        root.left = None
    else:
        prune(root.left)

    if is_all_zeros(root.right):
        root.right = None
    else:
        prune(root.right)

root = Node(0, left=Node(1), right=Node(0, left=Node(1, left=Node(0), right=Node(0)), right=Node(0)))
prune(root)
root.print_levels()
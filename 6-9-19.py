from node import Node

def BST_from_postorder_traversal(traversal):
    if len(traversal) == 0:
        return None

    root = traversal[-1]
    i = 0
    while traversal[i] < root:
        i += 1

    left_traversal = traversal[:i]
    right_traversal = traversal[i:-1]
    return Node(root,
                left=BST_from_postorder_traversal(left_traversal),
                right=BST_from_postorder_traversal(right_traversal))

traversal = [2, 4, 3, 8, 7, 5]
expected = Node(5, left=Node(3, left=Node(2), right=Node(4)), right=Node(7, right=Node(8)))
actual = BST_from_postorder_traversal(traversal)
assert expected == actual

traversal = [1, 2, 3]
expected = Node(3, left=Node(2, left=Node(1)))
actual = BST_from_postorder_traversal(traversal)
assert expected == actual
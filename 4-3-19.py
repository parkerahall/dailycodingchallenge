from node import Node

def lowest_common_ancestor(root, left, right):
    left_ancestors = set()
    right_ancestors = set()

    curr_left = left
    curr_right = right
    while curr_left != None or curr_right != None:
        if curr_left != None:
            if curr_left.value in right_ancestors:
                return curr_left.value
            left_ancestors.add(curr_left.value)
            curr_left = curr_left.parent

        if curr_right != None:
            if curr_right.value in left_ancestors:
                return curr_right.value
            right_ancestors.add(curr_right.value)
            curr_right = curr_right.parent
    return None

root = Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))
left = root.right.left
right = root.right.right
assert lowest_common_ancestor(root, left, right) == 3
assert lowest_common_ancestor(root, right, left) == 3


left = root
right = root.left
assert lowest_common_ancestor(root, left, right) == 1
assert lowest_common_ancestor(root, right, left) == 1
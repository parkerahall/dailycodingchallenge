from node import Node

def num_unival(root):
    
    def num_and_is_unival(root):
        if root == None:
            return 0, True

        left_num, left_unival = num_and_is_unival(root.left)
        right_num, right_unival = num_and_is_unival(root.right)

        if root.left == None and root.right == None:
            match = True
        elif root.left == None:
            match = root.value == root.right.value
        elif root.right == None:
            match = root.value == root.left.value
        else:
            match = (root.value == root.left.value) and (root.value == root.right.value)

        is_unival = left_unival and right_unival and match
        num_sub = left_num + right_num
        if is_unival:
            num_sub += 1

        return num_sub, is_unival
    
    num, is_unival = num_and_is_unival(root)
    return num

root = Node(0, left=Node(1), right=Node(0, left=Node(1, left=Node(1), right=Node(1)), right=Node(0)))
assert num_unival(root) == 5

root = Node(0)
assert num_unival(root) == 1

root = Node(0, left=Node(0))
assert num_unival(root) == 2

root = Node(0, left=Node(0), right=Node(1))
assert num_unival(root) == 2

root = Node(1, left=Node(1), right=Node(1))
assert num_unival(root) == 3
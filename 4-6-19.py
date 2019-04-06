from node import Node

def is_a_subtree(target, subtree):
    if subtree == target:
        return True
    elif target == None:
        return False
    return is_a_subtree(target.left, subtree) or is_a_subtree(target.right, subtree)

target = Node(1, left=Node(2, left=Node(6)), right=Node(3, left=Node(4), right=Node(5)))
subtree = target.right
assert is_a_subtree(target, subtree) == True

subtree = Node(2, left=Node(6))
assert is_a_subtree(target, subtree) == True

subtree = Node(3, left=Node(4))
assert is_a_subtree(target, subtree) == False

subtree = Node(1)
assert is_a_subtree(target, subtree) == False

assert is_a_subtree(target, target) == True
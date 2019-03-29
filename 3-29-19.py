from node import Node

def print_tree_levelwise(root):
    values = []
    frontier = [root]
    while len(frontier) > 0:
        new_frontier = []
        for node in frontier:
            values.append(node.value)
            if node.left != None:
                new_frontier.append(node.left)
            if node.right != None:
                new_frontier.append(node.right)
        frontier = new_frontier
    print(values)
    return values

root = Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))
assert print_tree_levelwise(root) == [1, 2, 3, 4, 5]
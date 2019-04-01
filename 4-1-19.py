from node import Node

def all_paths(root):
    paths = []
    current = []

    def all_paths_recur(root):
        current.append(root.value)
        if root.left == None and root.right == None:
            paths.append(current[:])

        if root.left != None:
            all_paths_recur(root.left)

        if root.right != None:
            all_paths_recur(root.right)

        current.pop()
    
    all_paths_recur(root)
    return paths

root = Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))
expected = [[1, 2], [1, 3, 4], [1, 3, 5]]
actual = all_paths(root)
assert set([tuple(x) for x in actual]) == set([tuple(x) for x in expected])
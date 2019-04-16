from node import Node

def search_for_K_sum(root, K):
    seen = set()
    current = [root]
    while len(current) > 0:
        new = []
        for node in current:
            if K - node.value in seen:
                return (node.value, K - node.value)
            else:
                seen.add(node.value)

            if node.left != None:
                new.append(node.left)
            if node.right != None:
                new.append(node.right)
        current = new
    return None

root = Node(10, left=Node(5), right=Node(15, left=Node(11), right=Node(15)))
K = 20
expected = (5, 15)
actual = search_for_K_sum(root, K)
assert set(actual) == set(expected)

root = Node(10, left=Node(5), right=Node(15, left=Node(11), right=Node(15)))
K = 30
expected = (15, 15)
actual = search_for_K_sum(root, K)
assert set(actual) == set(expected)

root = Node(10, left=Node(5), right=Node(15, left=Node(11), right=Node(15)))
K = 12
assert search_for_K_sum(root, K) == None
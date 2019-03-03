from node import Node

def deepest_node(root):
    def dn_helper(node):
        if node.left == None and node.right == None:
            return node, 1

        left_deepest, left_depth = dn_helper(node.left) if node.left != None else (None, 0)
        right_deepest, right_depth = dn_helper(node.right) if node.right != None else (None, 0)

        if left_deepest == None or right_depth >= left_depth:
            return right_deepest, right_depth + 1

        if right_deepest == None or left_depth >= right_depth:
            return left_deepest, left_depth + 1

    deepest, _ = dn_helper(root)
    return deepest

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.left = b
a.right = c
b.parent = a
c.parent = a

b.left = d
d.parent = b

assert deepest_node(a).value == "d"
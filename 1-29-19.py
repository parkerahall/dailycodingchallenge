class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return "Node(value:" + str(self.value) + ")"

def pretty_print_tree(root):
    levels = [[(root, root.parent)]]
    while len(levels[-1]) > 0:
        next_level = []
        for node, _ in levels[-1]:
            if node.left != None:
                next_level.append((node.left, node.value))
            if node.right != None:
                next_level.append((node.right, node.value))
        levels.append(next_level)
    levels.pop()

    for level in levels:
        print_tuples = [str((node.value, parent_value)) for (node, parent_value) in level]
        print " ".join(print_tuples)

def construct_tree(preorder, inorder):
    
    def construct_tree_recursive(root, preorder, inorder):
        i = 0
        while inorder[i] != root.value:
            i += 1

        left_inorder = inorder[:i]
        right_inorder = inorder[i + 1:]

        if len(left_inorder) > 0:
            left_set = set(left_inorder)
            left_preorder = [elt for elt in preorder if elt in left_set]

            left_subroot = Node(left_preorder[0], parent=root)
            root.left = left_subroot

            construct_tree_recursive(left_subroot, left_preorder, left_inorder)

        if len(right_inorder) > 0:
            right_set = set(right_inorder)
            right_preorder = [elt for elt in preorder if elt in right_set]

            right_subroot = Node(right_preorder[0], parent=root)
            root.right = right_subroot

            construct_tree_recursive(right_subroot, right_preorder, right_inorder)

    root = Node(preorder[0])
    construct_tree_recursive(root, preorder, inorder)
    return root

preorder = ["a", "b", "d", "e", "c", "f", "g"]
inorder = ["d", "b", "e", "a", "f", "c", "g"]
root = construct_tree(preorder, inorder)
pretty_print_tree(root)
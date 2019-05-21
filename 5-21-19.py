class MultiNode:
    def __init__(self, value, children=None, parent=None):
        children = children if children != None else []

        self.value = value
        self.children = children
        self.parent = parent

        for child in children:
            child.parent = self

    def print_levels(self):
        current = [self]
        while len(current) > 0:
            print([node.value for node in current])
            new = []
            for node in current:
                new.extend(node.children)
            current = new

def longest_path(root, weights):
    path_dict = {}

    def find_path_lengths(root):
        if root == None:
            return {}

        total_paths = {root.value: 0}
        child_paths = [(child, find_path_lengths(child)) for child in root.children]

        for child, path in child_paths:
            for node_value in path:
                path_length = path[node_value] + weights[(root.value, child.value)]
                total_paths[node_value] = path_length
                path_dict[(node_value, root.value)] = path_length

        for i in range(len(child_paths)):
            left_child, left_path = child_paths[i]
            for j in range(i + 1, len(child_paths)):
                right_child, right_path = child_paths[j]

                connecting = weights[(root.value, left_child.value)] + weights[(root.value, right_child.value)]

                for left_value in left_path:
                    for right_value in right_path:
                        path_length = left_path[left_value] + right_path[right_value] + connecting
                        path_dict[(left_value, right_value)] = path_length

        return total_paths

    find_path_lengths(root)
    max_sum = -float('inf')
    for key in path_dict:
        max_sum = max(max_sum, path_dict[key])

    # print(path_dict)
    return max_sum

g = MultiNode('g')
h = MultiNode('h')
e = MultiNode('e', children=[g, h])
f = MultiNode('f')
d = MultiNode('d', children=[e, f])
b = MultiNode('b')
c = MultiNode('c')
a = MultiNode('a', children=[b, c, d])

pure_weights = {('a', 'b'): 3, ('a', 'c'): 5, ('a', 'd'): 8, ('d', 'e'): 2, ('d', 'f'): 4,
                ('e', 'g'): 1, ('e', 'h'): 1}
weights = {}
for key in pure_weights:
    value = pure_weights[key]
    weights[key] = value
    weights[key[::-1]] = value

assert longest_path(a, weights) == 17
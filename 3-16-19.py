from node import Node

def longest_path(root):
    path_dict = {}

    def find_path_lengths(root):
        if root == None:
            return {}

        total_paths = {root.value: root.value}
        left_paths = find_path_lengths(root.left)
        right_paths = find_path_lengths(root.right)

        for node in left_paths:
            total_paths[node] = left_paths[node] + root.value
            path_dict[(node, root.value)] = left_paths[node] + root.value

            for right_node in right_paths:
                path_dict[(node, right_node)] = left_paths[node] + right_paths[right_node] + root.value

        for node in right_paths:
            total_paths[node] = right_paths[node] + root.value
            path_dict[(node, root.value)] = right_paths[node] + root.value

        return total_paths

    find_path_lengths(root)
    max_sum = -float('inf')
    for key in path_dict:
        max_sum = max(max_sum, path_dict[key])

    return max_sum

a = Node(1)
b = Node(2)
c = Node(3)

a.right = c
a.left = b

assert longest_path(a) == 6

root = Node(10)
left = Node(2)
right = Node(10)
ll = Node(20)
lr = Node(1)
rr = Node(-25)
rrl = Node(3)
rrr = Node(4)

root.left = left
root.right = right

left.left = ll
left.right = lr

right.right = rr

rr.left = rrl
rr.right = rrr

assert longest_path(root) == 42
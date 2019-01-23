class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def node_equals(first, second):
    if first == None or second == None:
        if first == None and second == None:
            return True
        else:
            return False

    val_eq = first.val == second.val
    left_eq = node_equals(first.left, second.left)
    right_eq = node_equals(first.right, second.right)
    return val_eq and left_eq and right_eq

def serialize(root):
    if root == None:
        return ""
    left_string = serialize(root.left)
    right_string = serialize(root.right)
    return str(root.val) + "/" + str(len(left_string)) + "/" + left_string + right_string

def deserialize(s):
    if len(s) == 0:
        return None
    end_value = s.find("/")
    value = s[:end_value]
    
    s = s[end_value + 1:]
    end_length = s.find("/")
    length = int(s[:end_length])

    s = s[end_length + 1:]
    left_string = s[:length]
    right_string = s[length:]
    return Node(value, deserialize(left_string), deserialize(right_string))

root = Node("root", Node("left", Node("left.left")), Node("right"))
s = serialize(root)
print(node_equals(root, deserialize(s)))
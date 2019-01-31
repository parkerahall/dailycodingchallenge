from node import Node

function_dict = { "+": lambda x,y : x + y,
                  "-": lambda x,y : x - y,
                  "*": lambda x,y : x * y,
                  "/": lambda x,y : x / y }

def evaluate(root):
    if type(root.value) == int:
        return root.value
    return function_dict[root.value](evaluate(root.left), evaluate(root.right))

root = Node("*")

left = Node("+")
right = Node("+")

ll = Node(3)
lr = Node(2)

rl = Node(4)
rr = Node(5)

# each Node object also has a parent field, but I chose not to initialize those because they are
# unnecessary for this problem
root.left = left
root.right = right

left.left = ll
left.right = lr

right.left = rl
right.right = rr

assert evaluate(root) == 45
class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        same_value = self.value == other.value
        
        same_left = True
        if self.left != None:
            if other.left == None:
                same_left = False
            else:
                same_left = self.left == other.left

        same_right = True
        if self.right != None:
            if other.right == None:
                same_right = False
            else:
                same_right = self.right == other.right

        return same_value and same_left and same_right
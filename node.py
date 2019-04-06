class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

        if left != None:
            left.parent = self

        if right != None:
            right.parent = self

    def print_levels(self):
        current = [self]
        while len(current) > 0:
            new = []
            print(" ".join([str(elt.value) for elt in current]))
            for elt in current:
                if elt.left != None:
                    new.append(elt.left)
                if elt.right != None:
                    new.append(elt.right)
            current = new

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        same_value = self.value == other.value
        
        same_left = True
        if self.left != None:
            same_left = self.left == other.left
        else:
            same_left = other.left == None

        same_right = True
        if self.right != None:
            same_right = self.right == other.right
        else:
            same_right = other.right == None

        return same_value and same_left and same_right
def calc_num_locked_subtree(node):
    return (node.num_lock_sub + (node.locked)) if node != None else 0

class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.locked = False
        self.num_lock_sub = calc_num_locked_subtree(left) + calc_num_locked_subtree(right)

    def is_locked(self):
        return self.locked

    def handle_change(self, is_locking):
        diff = 1 if is_locking else -1
        parent = self.parent
        while parent != None:
            parent.num_lock_sub += diff
            parent = parent.parent

    def lock(self):
        if self.num_lock_sub == 0:
            can_lock = True
            parent = self.parent
            while can_lock and parent != None:
                can_lock = can_lock and (not parent.locked)
                parent = parent.parent
            if can_lock:
                self.locked = True
                self.handle_change(True)
            return can_lock
        return False

    def unlock(self):
        if self.num_lock_sub == 0:
            can_unlock = True
            parent = self.parent
            while can_unlock and parent != None:
                can_unlock = can_unlock and (not parent.locked)
                parent = parent.parent
            if can_unlock:
                self.locked = False
                self.handle_change(False)
            return can_unlock
        return False

root = Node(1)
left = Node(2)
right = Node(3)
ll = Node(4)
lr = Node(5)
rl = Node(6)
rr = Node(7)

root.left = left
root.right = right
left.parent = root
right.parent = root

left.left = ll
left.right = lr
ll.parent = left
lr.parent = left

right.left = rl
right.right = rr
rl.parent = right
rr.parent = right

assert root.lock() == True
for elt in [left, right, ll, lr, rl, rr]:
    assert elt.lock() == False
assert root.unlock() == True

assert left.lock() == True
for elt in [root, ll, lr]:
    assert elt.lock() == False
for elt in [right, rl, rr]:
    assert elt.lock() == True
    assert elt.unlock() == True
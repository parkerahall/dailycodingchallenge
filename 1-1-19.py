class LinkedList:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

# debugging purposes
def print_list(l):
    if l != None:
        print l.value
        print_list(l.next)

# modifies l in-place
def reverse(l):
    prev = None
    current = l
    while current != None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

def find_intersection(l1, l2):
    rev_l1 = reverse(l1)
    rev_l2 = reverse(l2)

    prev = None
    current_l1 = rev_l1
    current_l2 = rev_l2

    while current_l1.value == current_l2.value:
        prev = current_l1.value
        current_l1 = current_l1.next
        current_l2 = current_l2.next
        if current_l1 == None or current_l2 == None:
            break

    return prev

l1 = LinkedList(1, LinkedList(2, LinkedList(3)))
l2 = LinkedList(4, LinkedList(1, LinkedList(2, LinkedList(3))))
assert find_intersection(l1, l2) == 1

l1 = LinkedList(1, LinkedList(2, LinkedList(3)))
l2 = LinkedList(4, LinkedList(1, LinkedList(2, LinkedList(3))))
assert find_intersection(l2, l1) == 1

l1 = LinkedList(1, LinkedList(2, LinkedList(3)))
l2 = LinkedList(1, LinkedList(2, LinkedList(3)))
assert find_intersection(l1, l2) == 1

l1 = LinkedList(1, LinkedList(2, LinkedList(3)))
l2 = LinkedList(3, LinkedList(2, LinkedList(1)))
assert find_intersection(l1, l2) == None
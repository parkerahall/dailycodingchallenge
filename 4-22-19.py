class RandomLinkedList:
    def __init__(self, value, nxt=None, rand=None):
        self.value = value
        self.next = nxt
        self.rand = rand

    def elts(self):
        output = [self.value]
        if self.next != None:
            output.extend(self.next.elts())
        return output

    def rands(self):
        output = [(self.value, self.rand.value)]
        if self.next != None:
            output.extend(self.next.rands())
        return output

def deep_clone(head):
    current = head
    while current != None:
        copy = RandomLinkedList(current.value, nxt=current.next)
        current.next = copy
        current = current.next.next
    
    current = head
    while current != None:
        current.next.rand = current.rand.next
        current = current.next.next

    current = head
    copy_head = head.next
    copy = head.next
    while current != None:
        current.next = current.next.next
        if copy.next != None:
            copy.next = copy.next.next

        current = current.next
        copy = copy.next

    return copy_head

fifth = RandomLinkedList(5)
fourth = RandomLinkedList(4, nxt=fifth)
third = RandomLinkedList(3, nxt=fourth)
second = RandomLinkedList(2, nxt=third)
first = RandomLinkedList(1, nxt=second)

first.rand = third
second.rand = first
third.rand = fifth
fourth.rand = third
fifth.rand = second

copy = deep_clone(first)
assert first.elts() == copy.elts()
assert first.rands() == copy.rands()
class LinkedList:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def reverse(head):
    if head == None:
        return head
    
    prev = None
    current = head
    nxt = current.next
    while nxt != None:
        current.next = prev
        prev = current
        current = nxt
        nxt = nxt.next
    return current

head = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
head = reverse(head)
i = 5
while head != None:
    assert head.value == i
    head = head.next
    i -= 1
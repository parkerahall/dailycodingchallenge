from linked_list import SinglyLinkedList

def rotate(head, k):
    length = 0
    current = head
    while current != None:
        length += 1
        current = current.next

    current = head
    new_tail = None
    new_head = None
    old_tail = None
    for i in range(length - 1):
        if i == length - k - 1:
            new_tail = current
        if i == length - k:
            new_head = current
        current = current.next
        if i == length - 2:
            old_tail = current

    new_tail.next = None
    old_tail.next = head
    return new_head

ll = SinglyLinkedList.from_list([7, 7, 3, 5])
k = 2
expected = SinglyLinkedList.from_list([3, 5, 7, 7])
assert rotate(ll, k) == expected

ll = SinglyLinkedList.from_list(list(range(1, 6)))
k = 3
expected = SinglyLinkedList.from_list([3, 4, 5, 1, 2])
assert rotate(ll, k) == expected
from linked_list import SinglyLinkedList as SLL

def swap_nodes(head):
    if head.next == None:
        return head

    new_head = head.next
    
    curr = head
    last = None
    while curr != None:
        if curr.next == None:
            break

        if last != None:
            last.next = curr.next

        next_next = curr.next.next
        curr.next.next = curr
        curr.next = next_next

        last = curr
        curr = curr.next

    return new_head

head = SLL(1, nxt=SLL(2, nxt=SLL(3, nxt=SLL(4))))
expected = SLL(2, nxt=SLL(1, nxt=SLL(4, nxt=SLL(3))))
actual = swap_nodes(head)
assert expected == actual

head = SLL(5, nxt=SLL(1, nxt=SLL(2, nxt=SLL(3, nxt=SLL(4)))))
expected = SLL(1, nxt=SLL(5, nxt=SLL(3, nxt=SLL(2, nxt=SLL(4)))))
actual = swap_nodes(head)
assert expected == actual
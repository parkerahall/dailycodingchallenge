from linked_list import SinglyLinkedList

def linked_list_sum(first, second):
    head = None
    current = None
    carry = 0
    while first != None or second != None or carry != 0:
        if first != None:
            first_num = first.value
            first = first.next
        else:
            first_num = 0

        if second != None:
            second_num = second.value
            second = second.next
        else:
            second_num = 0

        total = first_num + second_num + carry
        digit = total % 10
        carry = total / 10
        new_node = SinglyLinkedList(digit)
        
        if current != None:
            current.next = new_node

        if head == None:
            head = new_node
        
        current = new_node

    return head

first = SinglyLinkedList(1, nxt=SinglyLinkedList(2, nxt=SinglyLinkedList(3, nxt=SinglyLinkedList(4, nxt=SinglyLinkedList(5)))))
second = SinglyLinkedList(7, nxt=SinglyLinkedList(9, nxt=SinglyLinkedList(6)))
expected = SinglyLinkedList(8, nxt=SinglyLinkedList(1, nxt=SinglyLinkedList(0, nxt=SinglyLinkedList(5, nxt=SinglyLinkedList(5)))))
assert linked_list_sum(first, second) == expected

first = SinglyLinkedList(9, nxt=SinglyLinkedList(9))
second = SinglyLinkedList(5, nxt=SinglyLinkedList(2))
expected = SinglyLinkedList(4, nxt=SinglyLinkedList(2, nxt=SinglyLinkedList(1)))
assert linked_list_sum(first, second) == expected
from linked_list import *

def reverse(head, length):
    current = head
    next_node = head.next

    head.next = None
    while next_node != None and length > 1:
        next_next = next_node.next
        next_node.next = current
        current = next_node
        next_node = next_next
        length -= 1

    return current

def is_palindrome_single(head):
    length = 0
    current = head
    while current != None:
        length += 1
        current = current.next

    if length == 1:
        return True

    half = length / 2
    second_half = head
    for i in range(half + length % 2):
        second_half = second_half.next

    first_half = reverse(head, half)
    while first_half != None and second_half != None:
        if first_half.value != second_half.value:
            return False

        first_half = first_half.next
        second_half = second_half.next

    if first_half == None and second_half == None:
        return True
    return False

def is_palindrome_double(head):
    length = 0
    current = head
    while current != None:
        length += 1
        current = current.next

    if length == 1:
        return True

    half = length / 2
    first_half = head
    for i in range(half - 1):
        first_half = first_half.next

    second_half = first_half.next
    if length % 2:
        second_half = second_half.next

    while first_half != None and second_half != None:
        if first_half.value != second_half.value:
            return False

        first_half = first_half.prev
        second_half = second_half.next

    if first_half == None and second_half == None:
        return True
    return False

head = SinglyLinkedList(1, nxt=SinglyLinkedList(2, nxt=SinglyLinkedList(3, nxt=SinglyLinkedList(2, nxt=SinglyLinkedList(1)))))
assert is_palindrome_single(head) == True

head = SinglyLinkedList(3, nxt=(SinglyLinkedList(1, nxt=SinglyLinkedList(2, nxt=SinglyLinkedList(3, nxt=SinglyLinkedList(3, nxt=SinglyLinkedList(2, nxt=SinglyLinkedList(1, nxt=SinglyLinkedList(3)))))))))
assert is_palindrome_single(head) == True

head = SinglyLinkedList(1)
assert is_palindrome_single(head) == True

head = SinglyLinkedList(1, nxt=SinglyLinkedList(2))
assert is_palindrome_single(head) == False

head = SinglyLinkedList(3, nxt=(SinglyLinkedList(1, nxt=SinglyLinkedList(2, nxt=SinglyLinkedList(3, nxt=SinglyLinkedList(3, nxt=SinglyLinkedList(1, nxt=SinglyLinkedList(2, nxt=SinglyLinkedList(3)))))))))
assert is_palindrome_single(head) == False

head = DoublyLinkedList(1, nxt=DoublyLinkedList(2, nxt=DoublyLinkedList(3, nxt=DoublyLinkedList(2, nxt=DoublyLinkedList(1)))))
assert is_palindrome_double(head) == True

head = DoublyLinkedList(3, nxt=(DoublyLinkedList(1, nxt=DoublyLinkedList(2, nxt=DoublyLinkedList(3, nxt=DoublyLinkedList(3, nxt=DoublyLinkedList(2, nxt=DoublyLinkedList(1, nxt=DoublyLinkedList(3)))))))))
assert is_palindrome_double(head) == True

head = DoublyLinkedList(1)
assert is_palindrome_double(head) == True

head = DoublyLinkedList(1, nxt=DoublyLinkedList(2))
assert is_palindrome_double(head) == False

head = DoublyLinkedList(3, nxt=(DoublyLinkedList(1, nxt=DoublyLinkedList(2, nxt=DoublyLinkedList(3, nxt=DoublyLinkedList(3, nxt=DoublyLinkedList(1, nxt=DoublyLinkedList(2, nxt=DoublyLinkedList(3)))))))))
assert is_palindrome_double(head) == False
from linked_list import SinglyLinkedList

def find_length(linked_list):
    length = 0
    curr = linked_list
    while curr != None:
        curr = curr.next
        length += 1
    return length

# used for debugging
def print_length(head, length):
    l = []
    while head != None and length > 0:
        l.append(head.value)
        head = head.next
        length -= 1
    print(l)

def merge_portion(prev, head, length):
    first_head = head

    second_head = head
    for _ in range(length / 2):
        second_head = second_head.next

    last_last = head
    for _ in range(length):
        last_last = last_last.next

    first_moves = 0
    second_moves = 0
    new_head = None
    curr = new_head
    while first_moves + second_moves < length:
        if first_moves == length / 2:
            curr.next = second_head
            second_moves = length / 2
        elif second_moves == length / 2:
            curr.next = first_head
            first_moves = length / 2
        elif first_head.value < second_head.value:
            if new_head == None:
                new_head = first_head
                curr = first_head
            else:
                curr.next = first_head
                curr = curr.next
            first_head = first_head.next
            first_moves += 1
        else:
            if new_head == None:
                new_head = second_head
                curr = second_head
            else:
                curr.next = second_head
                curr = curr.next
            second_head = second_head.next
            second_moves += 1

    if prev != None:
        prev.next = new_head
    last = new_head
    for _ in range(length - 1):
        last = last.next
    
    return new_head, last, last_last
    

# assumes length of linked_list is a power of 2
def merge_sort(head):
    n = find_length(head)
    curr = head
    length = 2
    while length <= n:
        prev = None
        new_head = None
        for _ in range(n / length):
            portion_head, prev, curr = merge_portion(prev, curr, length)
            if new_head == None:
                new_head = portion_head
        prev.next = None
        curr = new_head

        length *= 2
    return curr

head = SinglyLinkedList(4, nxt=SinglyLinkedList(1, nxt=SinglyLinkedList(3, nxt=SinglyLinkedList(99))))
expected = head = SinglyLinkedList(1, nxt=SinglyLinkedList(3, nxt=SinglyLinkedList(4, nxt=SinglyLinkedList(99))))
actual = merge_sort(head)
assert actual == expected

second_half = SinglyLinkedList(4, nxt=SinglyLinkedList(1, nxt=SinglyLinkedList(3, nxt=SinglyLinkedList(99))))
head = SinglyLinkedList(101, nxt=SinglyLinkedList(-1, nxt=SinglyLinkedList(-7, nxt=SinglyLinkedList(2, nxt=second_half))))
second_expected = SinglyLinkedList(3, nxt=SinglyLinkedList(4, nxt=SinglyLinkedList(99, nxt=SinglyLinkedList(101))))
expected = SinglyLinkedList(-7, nxt=SinglyLinkedList(-1, nxt=SinglyLinkedList(1, nxt=SinglyLinkedList(2, nxt=second_expected))))
actual = merge_sort(head)
assert actual == expected
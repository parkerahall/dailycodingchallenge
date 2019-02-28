class LinkedList:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt
        self.tail = self if nxt == None else nxt.tail

    def add(self, node):
        self.tail.next = node
        self.tail = node

def get_value(linked_list, default):
    if linked_list == None:
        return default
    return linked_list.value

def merge_sorted_lists(lists):
    default = None
    
    merged = LinkedList("start")

    while True:
        best_value = None
        best_index = None
        for i in range(len(lists)):
            curr_list = lists[i]
            curr_value = get_value(curr_list, default)

            if (curr_value != default) and (best_value == None or curr_value < best_value):
                best_value = curr_value
                best_index = i

        if best_value == None:
            break
        else:
            merged.add(LinkedList(lists[best_index].value))
            lists[best_index] = lists[best_index].next

    merged = merged.next
    return merged

l1 = LinkedList(1)
l2 = LinkedList(-2, LinkedList(5))
l3 = LinkedList(-4, LinkedList(-3, LinkedList(0)))
l4 = LinkedList(4, LinkedList(12))
l5 = LinkedList(100)

expected = [-4, -3, -2, 0, 1, 4, 5, 12, 100]
merged = merge_sorted_lists([l1, l2, l3, l4, l5])
for i in range(len(expected)):
    assert merged.value == expected[i]
    merged = merged.next
assert merged == None
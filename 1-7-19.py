class LinkedList:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def check_list(ll, l):
    ind = 0
    while ll != None:
        assert ll.value == l[ind]
        ind += 1
        ll = ll.next

def rem_kth_last(linked_list, k):
    minus_one = None
    plus_one = None
    ind = 0
    head = linked_list
    while linked_list != None:
        if ind == k + 1:
            minus_one = head
            plus_one = head.next.next
        elif ind > k + 1:
            minus_one = minus_one.next
            plus_one = plus_one.next
        ind += 1
        last = linked_list
        linked_list = linked_list.next
    
    if minus_one == None:
        return head.next
    else:
        minus_one.next = plus_one
        return head

for i in range(5):
    ll = LinkedList(1, nxt=LinkedList(2, nxt=LinkedList(3, nxt=LinkedList(4, nxt=LinkedList(5)))))
    ll = rem_kth_last(ll, i)
    check_list(ll, [j for j in range(1, 6) if j != 5 - i])
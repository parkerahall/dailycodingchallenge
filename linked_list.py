class SinglyLinkedList:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def copy(self):
        nxt = self.next.copy() if self.next != None else None
        return SLL(self.value, nxt=nxt)

    def __eq__(self, other):
        if not isinstance(other, SinglyLinkedList):
            return False

        if self.value != other.value:
            return False
        
        return self.next == other.next

    def __str__(self):
        l = []
        curr = self
        while curr != None:
            l.append(curr.value)
            curr = curr.next
        return str(l)

    def __repr__(self):
        return srt(self)

class DoublyLinkedList:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt

        if nxt != None:
            nxt.prev = self

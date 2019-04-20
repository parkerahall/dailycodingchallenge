class SinglyLinkedList:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def __eq__(self, other):
        if not isinstance(other, SinglyLinkedList):
            return False

        if self.value != other.value:
            return False
        
        return self.next == other.next

class DoublyLinkedList:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt

        if nxt != None:
            nxt.prev = self

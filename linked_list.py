class SinglyLinkedList:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

class DoublyLinkedList:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt

        if nxt != None:
            nxt.prev = self
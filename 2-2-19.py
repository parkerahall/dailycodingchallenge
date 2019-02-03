class LinkedListNode:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = nxt

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def remove(self, node):
        if node.next != None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        if node.prev != None:
            node.prev.next = node.next
        else:
            self.head = node.next

    def add_node_front(self, node):
        node.prev = None
        node.next = self.head

        if self.head != None:
            self.head.prev = node
        if self.tail == None:
            self.tail = node
        self.head = node


class LRU_Cache:
    def __init__(self, n):
        self.size = n
        self.list = LinkedList()
        self.entries = {}

    def set(self, key, value):
        if key in self.entries:
            key_node = self.entries[key]
            key_node.value = value
            self.list.remove(key_node)
            self.list.add_node_front(key_node)
        else:
            key_node = LinkedListNode(key, value)
            self.list.add_node_front(key_node)
            self.entries[key] = key_node
            if len(self.entries) > self.size:
                remove_key = self.list.tail.key
                self.list.remove(self.list.tail)
                del self.entries[remove_key]

    def get(self, key):
        if key in self.entries:
            key_node = self.entries[key]
            value = key_node.value
            self.list.remove(key_node)
            self.list.add_node_front(key_node)
            return value
        else:
            print "Key not found in cache: " + str(key)

cache = LRU_Cache(5)
for i in range(6):
    cache.set(i, i)
for i in range(6):
    cache.get(i)
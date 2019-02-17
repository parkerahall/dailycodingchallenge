class LinkedListNode:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.freq = 0
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

class LFU_Cache:
    def __init__(self, n):
        self.num_elts = 0
        self.size = n
        self.cache = {}
        self.entries = {}

    def add_to_cache(self, node):
        node.freq += 1
        if node.freq not in self.cache:
            self.cache[node.freq] = LinkedList()
        self.cache[node.freq].add_node_front(node)
        self.entries[node.key] = node

    def set(self, key, value):
        if key in self.entries:
            key_node = self.entries[key]
            key_node.value = value
            self.cache[key_node.freq].remove(key_node)
            if self.cache[key_node.freq].head == None:
                del self.cache[key_node.freq]
            self.add_to_cache(key_node)
        else:
            key_node = LinkedListNode(key, value)
            self.add_to_cache(key_node)
            if self.num_elts > self.size:
                least_frequent = min(self.cache)
                lf_linked_list = self.cache[least_frequent]
                lf_linked_list.remove(lf_linked_list.tail)
                if self.cache[least_frequent].head == None:
                    del self.cache[least_frequent]

    def get(self, key):
        if key in self.entries:
            key_node = self.entries[key]
            value = key_node.value
            self.cache[key_node.freq].remove(key_node)
            if self.cache[key_node.freq].head == None:
                del self.cache[key_node.freq]
            self.add_to_cache(key_node)
            return value
        else:
            print "Key not found in cache: " + str(key)

N = 5
cache = LFU_Cache(N)
for i in range(N):
    cache.set(i, i)
cache.get(0)
cache.get(1)

for i in range(N - 1):
    cache.set(N + i, N + i)

assert cache.get(1) == 1
for i in range(N - 1):
    assert cache.get(N + i) == N + i


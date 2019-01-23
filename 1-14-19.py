class Heap:
    # cmp_func should determine validity of heap when passed (parent, child)
    # for example, max heap should have >= as cmp_func
    def __init__(self, cmp_func):
        self.heap = []
        self.cmp = cmp_func

    def reheapify_up(self, index):
        if index == 0:
            return
        
        child = index
        parent = (index - 1) / 2
        other_child = index + (1 if index % 2 else -1)
        if not self.cmp(self.heap[parent], self.heap[child]):
            # check that other child exists / index isn't out of bounds
            if other_child < len(self.heap):
                if self.cmp(self.heap[child], self.heap[other_child]):
                    self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                else:
                    self.heap[parent], self.heap[other_child] = self.heap[other_child], self.heap[parent]
            else:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            self.reheapify_up(parent)

    def reheapify_down(self, index):
        if index >= len(self.heap) / 2:
            return

        parent = index
        child = index * 2 + 1
        other_child = index * 2 + 2
        # check that other child exists / isn't out of bounds
        if other_child < len(self.heap):
            if (not self.cmp(self.heap[parent], self.heap[child])) or (not self.cmp(self.heap[parent], self.heap[other_child])):
                if self.cmp(self.heap[child], self.heap[other_child]):
                    self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                    self.reheapify_down(child)
                else:
                    self.heap[parent], self.heap[other_child] = self.heap[other_child], self.heap[parent]
                    self.reheapify_down(other_child)
        else:
            if not self.cmp(self.heap[parent], self.heap[child]):
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                self.reheapify_down(child)

    def add(self, elt):
        self.heap.append(elt)
        index = len(self.heap) - 1
        self.reheapify_up(index)

    def peek(self):
        return self.heap[0]

    def pop(self):
        last_index = len(self.heap) - 1
        self.heap[0], self.heap[last_index] = self.heap[last_index], self.heap[0]
        return_val = self.heap.pop()
        self.reheapify_down(0)
        return return_val

    def length(self):
        return len(self.heap)

def running_median(sequence):
    # max heap for all elements less than median
    max_heap = Heap(lambda x, y: x >= y)
    max_heap.add(-float("inf"))

    # min heap for all elements greater than or equal to median
    min_heap = Heap(lambda x, y: x <= y)
    min_heap.add(float("inf"))
    
    for elt in sequence:
        if max_heap.length() == 0 and min_heap.length() == 0:
            min_heap.add(elt)
        else:
            if elt > max_heap.peek():
                min_heap.add(elt)
                if min_heap.length() - max_heap.length() > 1:
                    switch = min_heap.pop()
                    max_heap.add(switch)
            else:
                max_heap.add(elt)
                if max_heap.length() > min_heap.length():
                    switch = max_heap.pop()
                    min_heap.add(switch)

        if (max_heap.length() + min_heap.length()) % 2:
            print min_heap.peek()
        else:
            print float(min_heap.peek() + max_heap.peek()) / 2

sequence = [2, 1, 5, 7, 2, 0, 5]
running_median(sequence)
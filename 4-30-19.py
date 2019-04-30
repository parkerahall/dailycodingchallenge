class PeekableInterface:
    def __init__(self, iterator):
        self.next_elt = None
        self.iterator = iterator

    def peek(self):
        if self.next_elt == None:
            self.next_elt = self.iterator.next()
        return self.next_elt

    def next(self):
        if self.next_elt != None:
            output = self.next_elt
            self.next_elt = None
        else:
            output = self.iterator.next()
        return output

    def hasNext(self):
        return self.next_elt != None or self.iterator.hasNext()

class IteratorInterface:
    def __init__(self, l):
        self.elts = l[::-1]

    def next(self):
        return self.elts.pop()

    def hasNext(self):
        return len(self.elts) > 0

iterator = IteratorInterface(range(5))
peekable = PeekableInterface(iterator)
assert peekable.hasNext() == True
assert peekable.peek() == 0
assert peekable.next() == 0
assert peekable.peek() == 1
assert peekable.peek() == 1
assert peekable.next() == 1
assert peekable.next() == 2
assert peekable.hasNext() == True
assert peekable.next() == 3
assert peekable.peek() == 4
assert peekable.hasNext() == True
assert peekable.next() == 4
assert peekable.hasNext() == False
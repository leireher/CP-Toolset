class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    def append(self, x):
        node = x if type(x) is Node else Node(x)
        node.prev = self
        node.next = self.next
        if self.next is not None:
            self.next.prev = node
        self.next = node

    def prepend(self, x):
        node = x if type(x) is Node else Node(x)
        node.prev = self.prev
        node.next = self
        if self.prev is not None:
            self.prev.next = node
        self.prev = node

class LinkedList:
    def __init__(self, data=tuple()):
        self.head = None
        self.tail = None
        for d in data:
            self.append(d)

    def append(self, x):
        node = x if type(x) == Node else Node(x)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def prepend(self, x):
        node = x if type(x) == Node else Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insert_after(self, target, x):
        node = x if type(x) == Node else Node(x)
        target.append(x)
        if target == self.tail:
            self.tail = node

    def insert_before(self, target, x):
        node = x if type(x) == Node else Node(x)
        target.prepend(x)
        if target == self.head:
            self.head = node

    def search(self, x):
        pointer = self.head
        while pointer is not None:
            if pointer.data == x:
                break
            pointer = pointer.next
        return pointer

    def remove(self, x):
        node = x if type(x) == Node else self.search(x)
        if node is None:
            return
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

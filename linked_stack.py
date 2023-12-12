from stack import Stack


class LinkedStack(Stack):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None
        self.size_count = 0

    def push(self, element):
        new_node = self.Node(element)
        new_node.next = self.top
        self.top = new_node
        self.size_count += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            data = self.top.data
            self.top = self.top.next
            self.size_count -= 1
            return data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.size_count

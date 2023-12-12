from stack import Stack


class ArrayStack(Stack):
    def __init__(self, capacity):
        self.elements = [None] * capacity
        self.top = -1

    def push(self, element):
        if self.top == len(self.elements) - 1:
            pass  # Handle stack full scenario
        else:
            self.top += 1
            self.elements[self.top] = element

    def pop(self):
        if self.is_empty():
            return None
        else:
            item = self.elements[self.top]
            self.top -= 1
            return item

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.elements[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

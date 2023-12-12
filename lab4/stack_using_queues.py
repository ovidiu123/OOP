from collections import deque
from stack import Stack


class StackUsingQueues(Stack):
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.size_count = 0

    def push(self, element):
        self.queue2.append(element)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.size_count += 1

    def pop(self):
        if self.is_empty():
            return None
        self.size_count -= 1
        return self.queue1.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self.queue1[0]

    def is_empty(self):
        return self.size_count == 0

    def size(self):
        return self.size_count

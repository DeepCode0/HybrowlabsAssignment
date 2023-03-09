class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_node = self.top
        self.top = popped_node.next
        popped_node.next = None
        return popped_node.value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None

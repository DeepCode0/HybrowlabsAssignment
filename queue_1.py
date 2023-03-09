class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        dequeued_node = self.front
        self.front = dequeued_node.next
        if self.front is None:
            self.back = None
        dequeued_node.next = None
        return dequeued_node.value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        return self.front is None

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example usage:
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

print("Queue:", queue.items)
print("Pop:", queue.pop())
print("Queue after pop:", queue.items)
print("Peek:", queue.peek())
print("Queue size:", queue.size())
print("Pop:", queue.pop())
print("Pop:", queue.pop())
print("Peek:", queue.peek())
print("Queue size:", queue.size())

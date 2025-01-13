class QueueUsingStacks:
    def __init__(self):  # Fixed constructor name
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None  # If both stacks are empty, return None

# Test
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1

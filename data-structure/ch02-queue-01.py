class ArrayQueue():
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0
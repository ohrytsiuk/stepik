class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.quantity = 0

    def can_add(self, v):
        return self.quantity + v <= self.capacity

    def add(self, v):
        self.quantity += v

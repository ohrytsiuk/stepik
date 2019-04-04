class Buffer:
    def __init__(self):
        self.array = []

    def add(self, *a):
        for arg in a:
            self.array.append(arg)
        while len(self.array) >= 5:
            total = 0
            for i in range(5):
                total += self.array[i]
            self.array.pop(4)
            self.array.pop(3)
            self.array.pop(2)
            self.array.pop(1)
            self.array.pop(0)
            print(total)

    def get_current_part(self):
        return self.array

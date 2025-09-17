# parent = (index - 1) / 2
# l-child = parent * 2 + 1
# r-child = parent * 2 + 2

#   0   1   
# [20, 10, ]

class Heap:
    def __init__(self):

        self.items = [0] * 10 
        self.size = 0

    def parent(self, index):
        return (index - 1) // 2
    
    def bubble_up(self):
        index = self.size - 1
        while((index > 0 and self.items[index] > self.items[self.parent(index)])):
            self.items[index], self.items[self.parent(index)] = self.items[self.parent(index)], self.items[index]
            index = self.parent(index)

    def insert(self, val):
        if self.size == len(self.items):
            return "Heap is full"

        self.items[self.size] = val
        self.size += 1
        self.bubble_up()
        print(self.items)


h = Heap()
h.insert(20)
h.insert(10)
h.insert(17)
h.insert(18)

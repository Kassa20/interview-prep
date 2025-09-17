
``` python
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
    
    def left_child_index(self, index):
        return index*2 + 1
    
    def right_child_index(self, index):
        return index*2 + 2
    
    def has_left_child(self, index):
        return self.left_child_index(index) <= self.size
    
    def has_right_child(self, index):
        return self.right_child_index(index) <= self.size
    
    def left_child(self, index):
        return self.items[self.left_child_index(index)]
    
    def right_child(self, index):
        return self.items[self.right_child_index(index)]
    
    def is_valid_parent(self, index):
        if not self.has_left_child(index):
            return True
        
        if not self.has_right_child(index):
            return self.items[index] >= self.left_child(index)

        return (self.items[index] >= self.left_child(index) and 
                self.items[index] >= self.right_child(index))
    
    def larger_child_index(self, index):
        if not self.has_left_child(index):
            return index
        
        if not self.right_child(index):
            return self.left_child_index(index)

        return self.left_child_index(index) if self.left_child(index) > self.right_child(index) else self.right_child_index(index)

    
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


    def remove(self):

        if self.size == 0:
            return "heap is empty"

        self.items[0] = self.items[self.size - 1]
        self.size -= 1

        index = 0
        while index <= self.size and self.is_valid_parent(index) is False:
            larger_child_index = larger_child_index(index)
            larger_child_index, index = index, larger_child_index
            index = larger_child_index

```
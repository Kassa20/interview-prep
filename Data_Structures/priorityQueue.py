class PriorityQueue:

    def __init__(self):
        self.items = [0] * 10
        self.size = 0

    def enqueue(self, value):
        if self.size == len(self.items):
            return "Queue is full"       

        index = -1   # if we are always adding in reverse,
                    # the element to be added will always be at index = -1+1 = 0
        for i in range(self.size-1, -1, -1):
            if self.items[i] > value:
                self.items[i + 1] = self.items[i]
            else:
                index = i
                break
        
        self.items[index + 1] = value
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("queue is empty")
            return
        
        for i in range(self.size):
            self.items[i] = self.items[i+1]
        self.items[self.size-1] = 0
        self.size -= 1

    def display(self):
        print(self.items)
    


q = PriorityQueue()
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.dequeue()
q.display()
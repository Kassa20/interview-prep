"""Singly linked list implementation"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def append(self, item):
        new_node = Node(data=item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1


    def prepend(self, item):
        new_node = Node(data=item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def delete(self, item):

        if self.is_empty():
            return "LinkedList is empty"
        
        # If removing head
        if self.head.data == item:
            self.head = self.head.next
            if self.head is None: #list became empty
                self.tail = None
            return
        
        left = self.head
        right = self.head.next
        

        

        
    def search(self, item):

        if self.is_empty():
            return "LinkedList is empty"
        
        walk = self.head

        while walk != None:
            if walk.data == item:
                return True
            walk = walk.next


    def display(self):
        res = []
        current = self.head
        while current:
            res.append(str(current.data))
            current = current.next
        print(" -> ".join(res))

            
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.display()            

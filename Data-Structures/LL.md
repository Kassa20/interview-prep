
# Implementation

# ```python

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

        curr = self.head
        while curr != None:
            if (curr.next == item and curr.next == self.tail):
                self.tail = curr
                self.tail.next = None
                return
            elif curr.next == item:
                curr.next = curr.next.next 
                return

            curr = curr.next
        
        
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

```



# Singly Linked List

```
append operation becomes O(1) if a tail pointer is added
if the LL is empty, both the head and tail are pointing to the new_node in memory, 
therefore tail.next = head.next. 

once we have 2 elements, the tail will point to the new_node at which point head will also point to new_node since they are pointing to the same new_node in memory initially.Then we assign tail as the new_node, the head is now free from the tail. Each new addiiton will thus no longer affect the head. The fact that both head and tail point to the new_node for a single element is important. 
```

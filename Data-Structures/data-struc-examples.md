# Stack

```
LIFO(last in first out)
S.push(e): Add element e to the top of stack S.
S.pop(): Remove and return the top element from the stack S; an error occurs if the stack is empty. Additionally, let us define the following accessor methods for convenience:
S.top(): Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
S.is empty(): Return True if stack S does not contain any elements.
len(S): Return the number of elements in stack S; in Python, we implement this with the special method len

```

# Implementation 

```python
class Stack:
    """Stack implementation using Array"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)

    def top(self):

        if self.is_empty():
            return "Stack is empty"
        return self._data[-1]
    
    def pop(self):

        if self.is_empty():
            return "Stack is empty"
        return self._data.pop()
```

# Queue

```
Queues

Another fundamental data structure is the queue. It is a close “cousin” of the stack,
as a queue is a collection of objects that are inserted and removed according to the
first-in, first-out (FIFO) principle. That is, elements can be inserted at any time,
but only the element that has been in the queue the longest can be next removed.

Use-Cases 
- Printers
- Web server responding requests 

In the implementation, the queue is a circular queue. This is to make the dequeue operation efficient 

queue.remove(first) is a O(n) operation 

![alt text](./images/image.png)

![alt text](./images/image-1.png)

```

# Implementation 

```python

class Queue:

    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        
        if self.is_empty():
            return "queue is empty"
        return self._data[self._first]

        
    def dequeue(self):

        if self.is_empty():
            return "queue is empty"
        
        res = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return res

    def enqueue(self, e):

        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        index = (self._front + self._size) % len(self._data)
        self._data[index] = e
        self._size += 1

    def resize(self, amount):

        old = self._data
        self._data = [None] * amount
        walk = self._front

        for i in range(len(old)):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

```

# Singly Linked List

```
append operation becomes O(1) if a tail pointer is added
if the LL is empty, both the head and tail are pointing to the new_node in memory, 
therefore tail.next = head.next. 

once we have 2 elements, the tail will point to the new_node at which point head will also point to new_node since they are pointing to the same new_node in memory initially.Then we assign tail as the new_node, the head is now free from the tail. Each new addiiton will thus no longer affect the head. The fact that both head and tail point to the new_node for a single element is important. 
```

# Implementation
```python

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

    #not finished
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

```



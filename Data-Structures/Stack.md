
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

# Stack
```
LIFO(last in first out)
S.push(e): Add element e to the top of stack S.
S.pop(): Remove and return the top element from the stack S; an error occurs if the stack is empty. Additionally, let us define the following accessor methods for convenience:
S.top(): Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
S.is empty(): Return True if stack S does not contain any elements.
len(S): Return the number of elements in stack S; in Python, we implement this with the special method len

```
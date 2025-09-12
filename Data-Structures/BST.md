# Implementation 
```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root


    def insert(self, data):

        if self.root == None:
            self.root = TreeNode(value=data)
            return

        curr = self.root
        while True:

            if data > curr.value:
                if curr.right == None:
                    curr.right = TreeNode(data)
                    break
                curr = curr.right
            
            else:
                if curr.left == None:
                    curr.left = TreeNode(data)
                    break
        
    
    
    def search(self, data):

        curr = self.root

        while curr != None:
            if data > curr.value:
                curr = curr.right
            elif data < curr.value:
                curr = curr.left
            else:
                return True
        
        return False


    def preOrder(self, root):

        if root == None:
            return
        
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

        return 
        
```

# Binary Search Trees


- DFS (depth first)

  - Add elements to a stack and while the stack is not empty pop a node and add all its
    children to the stack. Iterate until the stack is empty or all the nodes have been visited

    #### Traversals 
  - Pre-order: root, left, right
  - In-order: left, root, right
  - Post-order: left, right, root

- BFS (breadth first)
  - Exactly the same as dfs but using a queue
  - By its nature, bfs visites each node level by level. So bfs would be good for level order traversal
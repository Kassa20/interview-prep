Documenting all the important stuff I'm learning 

  # Table of contents

  
  ## Data-Structures (Theory)

   ### Arrays 
- Built from fixed-size records
- Constant access time given the index.
- Space efficient – arrays consist only of the data, so no space is wasted with links or formatting info.
- Easy to iterate over quickly, because of memory locality.
- Cannot adjust their size in the middle of a program's execution.
- Dynamic arrays double in size whenever insert index is out of bound (Java's ArrayList is dynamic, while int isn't).
- Java array max length is Integer.MAX_VALUE = 2^31-1 (but could actually be a bit shorter because of reserved memory).


   ### Linked Lists
- Singly-linked – each elements links to the next one.
- Doubly-linked – each elements links to the next and previous elements.
- Operations supported: search, insert, delete.
- Cannot overflow (as opposed to static arrays which have a finite length).
- Simpler insertion/deletion than arrays.
- Requires extra memory for pointers than arrays.
- Not efficient for random access to items.
- Worse memory locality than arrays.

   ### Stacks and Queues
- Stacks – LIFO (push, pop)
  - Very efficient, good to use when retrieval order doesn't matter at all (like for batch jobs).
  - LIFO usually happens in recursive algorithms.
- Queues – FIFO (enqueue, dequeue)
  - Average "waiting time" for jobs is identical for FIFO and LIFO. Maximum time varies (FIFO minimizes max waiting time).
  - Harder to implement, appropriate when order is important.
  - Used for searches in graphs.

  ### BST (order of traversal)
- DFS (depth first) 
  - Pre-order: root, left, right
  - In-order: left, root, right
  - Post-order: left, right, root
  - can be implemented using a stack
- BFS (breadth first)
  - Implemented using a queue, visit all nodes at current level, advance to next level (doesn't use recursion)


  ## Data-Structures (Implementation)
  
- [Stack](Data-Structures/Stack.md)
- [Queue](Data-Structures/Queue.md)
- [Linked-Lists](Data-Structures/LL.md)
- [Binary-Search-Tree](Data-Structures/BST.md)


   ### Array
- Built from fixed-size records
- Constant access time given the index.
- Space efficient – arrays consist only of the data, so no space is wasted with links or formatting info.
- Easy to iterate over quickly, because of memory locality.
- Cannot adjust their size in the middle of a program's execution.
- Dynamic arrays double in size whenever insert index is out of bound (Java's ArrayList is dynamic, while int isn't).
- Java array max length is Integer.MAX_VALUE = 2^31-1 (but could actually be a bit shorter because of reserved memory).


   ### Linked List
- Singly-linked – each elements links to the next one.
- Doubly-linked – each elements links to the next and previous elements.
- Operations supported: search, insert, delete.
- Cannot overflow (as opposed to static arrays which have a finite length).
- Simpler insertion/deletion than arrays.
- Requires extra memory for pointers than arrays.
- Not efficient for random access to items.
- Worse memory locality than arrays.

   ### Stack and Queue
- Stacks – LIFO (push, pop)
  - Very efficient, good to use when retrieval order doesn't matter at all (like for batch jobs).
  - LIFO usually happens in recursive algorithms.
- Queues – FIFO (enqueue, dequeue)
  - Average "waiting time" for jobs is identical for FIFO and LIFO. Maximum time varies (FIFO minimizes max waiting time).
  - Harder to implement, appropriate when order is important.
  - Used for searches in graphs.

  ### BST (order of traversal)



  ### Graph


  ### Heap
- We will store data as an array of keys, and use the position of the keys to implicitly satisfy the role of the pointers.
- The positions of the parent and children of the key at index i are readily determined. The left child of i sits in position 2i+1 and   the right child in 2i + 2, while the parent of k holds court in position floor(i-1/2).
- We always fill the heap from left to right. 
- Performing a search in a heap requires linear scanning – we can't do a log(n) search like in a binary search tree.
- All we know in a min-heap is that the child is larger than the parent, we don't know about the relationship between the children.
- To insert an item we add it at the end of the array, and then bubble it up if it's smaller that its parent (switch between the parent and the child), until we reach a smaller parent or the root of the tree. This insertion in O(log(n)).
- The minimum of the tree is the root. To extract it, we remove the root, and replace it with the last element in the array (bottom rightmost leaf). We then check if it's smaller than both its children. If not, we perform a swap with the smallest child, and bubble the swap down recursively all the way until the criteria is met. This is called "heapify". This operation requires O(log(n)).
- To build a heap from an array iterate from the last element to the first and call heapify on each. This costs O(n). 
- We start building from (n // 2) because this is the index where the last non leaf node exisits. 
- [https://youtu.be/HqPJF2L5h9U] (Video on heap)
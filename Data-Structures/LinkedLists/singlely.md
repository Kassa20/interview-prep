
append operation becomes O(1) if a tail pointer is added
if the LL is empty, both the head and tail are pointing to the new_node in memory, 
therefore tail.next = head.next. 

once we have 2 elements, the tail will point to the new_node at which point head will also point to new_node since they are pointing to the same new_node in memory initially.Then we assign tail as the new_node, the head is now free from the tail. Each new addiiton will thus no longer affect the head. The fact that both head and tail point to the new_node for a single element is important. 

from collections import deque

def bfs(self, node):

    if node not in self.adj_list.keys():
        return
    
    queue = deque()
    seen = set()
    queue.append(node)

    while queue:
        curr = queue.popleft()
        if curr in seen:
            continue    
        seen.add(curr)
        print(curr)

        for neighbor in self.adj_list[curr]:
            if neighbor not in seen:
                queue.append(neighbor)


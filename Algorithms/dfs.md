``` Python
def dfs(self, node):

    if node not in self.adj_list.keys():
        return

    stack = []
    seen = set()
    stack.append(node)

    while stack:
        curr = stack.pop()
        if curr in seen:       # avoid duplicates 
            continue
        print(curr)
        seen.add(curr)
        for neighbor in self.adj_list[curr]:
            if neighbor not in seen:        # just making the dfs faster, not necessary 
                stack.append(neighbor)
 
```
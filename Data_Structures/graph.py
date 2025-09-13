from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u, v):

        if u not in self.adj_list:
            self.add_node(u)
        
        if v not in self.adj_list:
            self.add_node(v)

        self.adj_list[u].append(v)


    def remove_node(self, node):
        
        if node in self.adj_list:
            
            for neighbors in self.adj_list.values():
                if node in neighbors:
                    neighbors.remove(node)

            del self.adj_list[node]

    def remove_edge(self, u, v):

        if (u in self.adj_list and v in self.adj_list[u]):
            self.adj_list[u].remove(v)


    def display(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node} -> {neighbors}")

"""
CS361 - HW3
Problem 2 - graph implementation (adjacency list)
Author: Shrey Poshiya
"""


class Graph:

    def __init__(self, v):
        """
        assumes integer graph verticies
        """
        self.v = v
        self.adj = {i: [] for i in range(v)}

    def add_directed_edge(self, u, w):
        assert 0 <= u < self.v and 0 <= w < self.v, "vertex out of range"

        self.adj[u].append(w)

    def add_undirected_edge(self, u, w):
        assert 0 <= u < self.v and 0 <= w < self.v, "vertex out of range"
        
        self.adj[u].append(w)
        self.adj[w].append(u)

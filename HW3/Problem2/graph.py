"""
CS361 - HW3
Problem 2 - Graph (adjacency list)
Author: Shrey Poshiya
"""


class Graph:

    def __init__(self, v):
        self.v = v
        self.adj = {i: [] for i in range(v)}

    def add_directed_edge(self, u, w):
        self._check(u, w)
        self.adj[u].append(w)

    def add_undirected_edge(self, u, w):
        self._check(u, w)
        self.adj[u].append(w)
        self.adj[w].append(u)

    def _check(self, u, w):
        assert 0 <= u < self.v and 0 <= w < self.v, "vertex out of range"

    def __str__(self):
        return "\n".join(f"{u}: {neighbors}" for u, neighbors in self.adj.items())

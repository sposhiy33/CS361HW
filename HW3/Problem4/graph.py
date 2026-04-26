"""
CS361 - HW3
Problem 4 - graph implementation (adjacency list and adjacency matrix)
Author: Shrey Poshiya
"""


class GraphList:

    def __init__(self, verticies):
        """
        verticies is a list of vertex labels (any hashable, e.g. ints or letters)
        """
        self.v = verticies
        self.adj = {label: [] for label in verticies}

    def add_directed_edge(self, u, w):
        assert u in self.adj and w in self.adj, "vertex not in graph"

        self.adj[u].append(w)

    def add_undirected_edge(self, u, w):
        assert u in self.adj and w in self.adj, "vertex not in graph"

        self.adj[u].append(w)
        self.adj[w].append(u)


class GraphMatrix:

    def __init__(self, verticies):
        """
        verticies is a list of vertex labels (any hashable, e.g. ints or letters)
        """
        self.v = verticies
        # map label -> row/col index so we can support non-integer labels
        self.idx = {label: i for i, label in enumerate(verticies)}
        n = len(verticies)
        self.adj = [[0 for _ in range(n)] for _ in range(n)]

    def add_directed_edge(self, u, w):
        assert u in self.idx and w in self.idx, "vertex not in graph"

        self.adj[self.idx[u]][self.idx[w]] = 1

    def add_undirected_edge(self, u, w):
        assert u in self.idx and w in self.idx, "vertex not in graph"

        self.adj[self.idx[u]][self.idx[w]] = 1
        self.adj[self.idx[w]][self.idx[u]] = 1

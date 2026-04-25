"""
CS361 - HW3
Problem 2 - Is the graph a tree?
Author: Shrey Poshiya
"""

from graph import Graph


def main():
    tree = Graph(5)
    tree.add_undirected_edge(0, 1)
    tree.add_undirected_edge(0, 2)
    tree.add_undirected_edge(1, 3)
    tree.add_undirected_edge(1, 4)

    not_tree = Graph(4)
    not_tree.add_undirected_edge(0, 1)
    not_tree.add_undirected_edge(1, 2)
    not_tree.add_undirected_edge(2, 0)
    not_tree.add_undirected_edge(2, 3)


if __name__ == "__main__":
    main()

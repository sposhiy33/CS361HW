"""
CS361 - HW3
Problem 2 - Is the graph a tree?
Author: Shrey Poshiya
"""

from graph import Graph
import random

def detectTree(graph) -> bool:
    """
    When traversing a tree, we should have EXACTLY
    ONE instance of a connection of the current node being
    in the visited list ... this is the parent. If more than 
    one connection is in the visited list, the structure of 
    the graph is not a tree.
    """ 

    # pick a source node (do random key)
    source = random.choice(list(graph.adj))

    # do a BFS traversal from the source
    # with an added check for a cycle
    visited = [source]
    queue = [source]

    while len(queue) > 0:

        node = queue.pop(0)
       
        # now do a check to see how many of its connections
        # are in the visited list, intersection
        if len(set(graph.adj[node]) & set(visited)) >= 2:
            return False

        # add the children to the queue
        for item in graph.adj[node]:
            if item not in visited:
                queue.append(item)
                visited.append(item)

        

    # make sure that the graph is connected
    if len(visited) == len(list(graph.adj)):
        return True
    else:
        return False


def main():

    #    0
    #  1   2
    # 3 4
    tree = Graph(5)
    tree.add_undirected_edge(0, 1)
    tree.add_undirected_edge(0, 2)
    tree.add_undirected_edge(1, 3)
    tree.add_undirected_edge(1, 4)
    print(f"Test Case 1: Tree")
    print(f"\t Result: {detectTree(tree)}")

    # same tree from above, with a cycle
    not_tree = Graph(5)
    not_tree.add_undirected_edge(0, 1)
    not_tree.add_undirected_edge(0, 2)
    not_tree.add_undirected_edge(1, 3)
    not_tree.add_undirected_edge(1, 4)
    not_tree.add_undirected_edge(3, 0)
    print(f"Test Case 1: Tree with a Cycle ... so not tree")
    print(f"\t Result: {detectTree(not_tree)}")


if __name__ == "__main__":
    main()

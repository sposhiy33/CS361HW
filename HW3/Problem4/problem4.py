"""
CS361 - HW3
Problem 4 - BFS and DFS implementation
Author: Shrey Poshiya
"""


def bfs_list(graph, source, target=None, verbose=True) -> list:
    """
    BFS for adj list representation of graph.
    Stops early when the target is reached (if given).
    Prints the length of the visited list when done.
    """

    assert source in graph.adj, "source not in graph"
    if target is not None:
        assert target in graph.adj, "target not in graph"

    visited = [source]
    queue = [source]

    while len(queue) > 0:

        node = queue.pop(0)
        if verbose:
            print(f"\t pop {node} from queue")

        # early stop if the target was reached
        if node == target:
            break

        # add the children to the queue
        for item in graph.adj[node]:
            if verbose:
                print(f"\t   traversed node {node} -> {item}")
            if item not in visited:
                queue.append(item)
                visited.append(item)

    if verbose:
        print(f"\t BFS List visited length: {len(visited)}\n")
    return visited


def bfs_matrix(graph, source, target=None, verbose=True) -> list:
    """
    BFS for adj matrix representation.
    Stops early when the target is reached (if given).
    Prints the length of the visited list when done.
    """
    assert source in graph.idx, "source not in graph"
    if target is not None:
        assert target in graph.idx, "target not in graph"

    visited = [source]
    queue = [source]

    while len(queue) > 0:

        node = queue.pop(0)
        if verbose:
            print(f"\t pop {node} from queue")

        if node == target:
            break

        # scan the row to find the children
        # use row since edge may be directed -- row will work for both
        for item in graph.v:
            if graph.adj[graph.idx[node]][graph.idx[item]] == 1:
                if verbose:
                    print(f"\t   traversed node {node} -> {item}")
                if item not in visited:
                    queue.append(item)
                    visited.append(item)

    if verbose:
        print(f"\t BFS Matrix visited length: {len(visited)}\n")
    return visited


def dfs_list(graph, source, target=None, verbose=True) -> list:
    """
    DFS for adj list representation of graph.
    Stops early when the target is reached (if given).
    Prints the length of the visited list when done.
    """
    assert source in graph.adj, "source not in graph"
    if target is not None:
        assert target in graph.adj, "target not in graph"

    visited = [source]
    stack = [source]

    while len(stack) > 0:

        node = stack.pop()
        if verbose:
            print(f"\t pop {node} from stack")

        if node == target:
            break

        # push the children onto the stack
        for item in graph.adj[node]:
            if verbose:
                print(f"\t   traversed node {node} -> {item}")
            if item not in visited:
                stack.append(item)
                visited.append(item)

    if verbose:
        print(f"\t DFS List visited length: {len(visited)}\n")
    return visited


def dfs_matrix(graph, source, target=None, verbose=True) -> list:
    """
    DFS for adj matrix representation.
    Stops early when the target is reached (if given).
    Prints the length of the visited list when done.
    """
    assert source in graph.idx, "source not in graph"
    if target is not None:
        assert target in graph.idx, "target not in graph"

    visited = [source]
    stack = [source]

    while len(stack) > 0:

        node = stack.pop()
        if verbose:
            print(f"\t pop {node} from stack")

        if node == target:
            break

        # scan the row to find the children
        # use row since edge may be directed -- row will work for both
        for item in graph.v:
            if graph.adj[graph.idx[node]][graph.idx[item]] == 1:
                if verbose:
                    print(f"\t   traversed node {node} -> {item}")
                if item not in visited:
                    stack.append(item)
                    visited.append(item)

    if verbose:
        print(f"\t DFS Matrix visited length: {len(visited)}\n")
    return visited

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

    found = source == target
    while len(queue) > 0 and not found:

        node = queue.pop(0)
        if verbose:
            print(f"\t pop {node} from queue")

        # add the children to the queue
        for item in graph.adj[node]:
            if verbose:
                print(f"\t   traversed node {node} -> {item}")
            if item not in visited:
                queue.append(item)
                visited.append(item)
                # early stop the moment the target is discovered
                if item == target:
                    found = True
                    break

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

    found = source == target
    while len(queue) > 0 and not found:

        node = queue.pop(0)
        if verbose:
            print(f"\t pop {node} from queue")

        # scan the row to find the children
        # use row since edge may be directed -- row will work for both
        for item in graph.v:
            if graph.adj[graph.idx[node]][graph.idx[item]] == 1:
                if verbose:
                    print(f"\t   traversed node {node} -> {item}")
                if item not in visited:
                    queue.append(item)
                    visited.append(item)
                    if item == target:
                        found = True
                        break

    if verbose:
        print(f"\t BFS Matrix visited length: {len(visited)}\n")
    return visited


def dfs_list(graph, source, target=None, verbose=True) -> list:
    """
    DFS for adj list representation of graph.
    Stops early when the target is reached (if given).
    Prints the length of the visited list when done.

    visited records the actual pop order (real DFS traversal), not push
    order -- otherwise the output reads BFS-like since neighbors are
    discovered in level order even when the stack processes them deeply.
    """
    assert source in graph.adj, "source not in graph"
    if target is not None:
        assert target in graph.adj, "target not in graph"

    visited = []
    stack = [source]

    while len(stack) > 0:

        node = stack.pop()
        # node may be on the stack twice if it was a neighbor of two
        # already-popped nodes -- skip the second pop
        if node in visited:
            continue
        visited.append(node)
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

    if verbose:
        print(f"\t DFS List visited length: {len(visited)}\n")
    return visited


def dfs_matrix(graph, source, target=None, verbose=True) -> list:
    """
    DFS for adj matrix representation.
    Stops early when the target is reached (if given).
    Prints the length of the visited list when done.

    visited records the actual pop order (real DFS traversal); see
    dfs_list for the rationale.
    """
    assert source in graph.idx, "source not in graph"
    if target is not None:
        assert target in graph.idx, "target not in graph"

    visited = []
    stack = [source]

    while len(stack) > 0:

        node = stack.pop()
        if node in visited:
            continue
        visited.append(node)
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

    if verbose:
        print(f"\t DFS Matrix visited length: {len(visited)}\n")
    return visited

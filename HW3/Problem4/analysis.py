"""
CS361 - HW3
Problem 4 - BFS and DFS analysis (graph examples, path-finding, time + memory)
Author: Shrey Poshiya
"""

import csv
import os
import time
import tracemalloc

from graph import GraphList, GraphMatrix
from problem4 import bfs_list, bfs_matrix, dfs_list, dfs_matrix


RESULTS_DIR = "results"
CSV_PATH = os.path.join(RESULTS_DIR, "analysis_results.csv")


def build_graph_undirected(GraphClass):

    g = GraphClass([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    g.add_undirected_edge(1, 3)
    g.add_undirected_edge(1, 2)
    g.add_undirected_edge(1, 4)
    g.add_undirected_edge(3, 5)
    g.add_undirected_edge(3, 0)
    g.add_undirected_edge(2, 0)
    g.add_undirected_edge(5, 7)
    g.add_undirected_edge(0, 7)
    g.add_undirected_edge(0, 8)
    g.add_undirected_edge(8, 10)
    g.add_undirected_edge(4, 6)
    g.add_undirected_edge(6, 9)
    g.add_undirected_edge(6, 11)
    g.add_undirected_edge(9, 11)
    return g


def build_graph_directed(GraphClass):

    g = GraphClass(['A', 'B', 'C', 'D', 'E', 'F', 'G',
                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'])
    g.add_directed_edge('A', 'B')
    g.add_directed_edge('A', 'C')
    g.add_directed_edge('B', 'D')
    g.add_directed_edge('B', 'G')
    g.add_directed_edge('C', 'D')
    g.add_directed_edge('D', 'E')
    g.add_directed_edge('E', 'F')
    g.add_directed_edge('E', 'K')
    g.add_directed_edge('F', 'G')
    g.add_directed_edge('F', 'H')
    g.add_directed_edge('F', 'M')
    g.add_directed_edge('G', 'H')
    g.add_directed_edge('G', 'L')
    g.add_directed_edge('G', 'N')
    g.add_directed_edge('G', 'K')
    g.add_directed_edge('H', 'I')
    g.add_directed_edge('I', 'J')
    g.add_directed_edge('J', 'H')
    g.add_directed_edge('J', 'D')
    g.add_directed_edge('K', 'L')
    g.add_directed_edge('K', 'F')
    g.add_directed_edge('M', 'O')
    g.add_directed_edge('N', 'O')
    return g


def measure(label, function, runs=5):
    """
    run function 'runs' times, return (avg time in us, avg peak memory in bytes)

    memory is captured via tracemalloc's peak counter -- the highest amount of
    memory tracked between tracemalloc.start() and get_traced_memory(). this
    captures working memory (visited, queue/stack, transient iterators) at the
    algorithm's peak, not just what survives after the call returns.
    """
    times = []
    peaks = []

    for _ in range(runs):
        tracemalloc.start()

        t0 = time.perf_counter()
        function()
        t1 = time.perf_counter()

        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        times.append(t1 - t0)
        peaks.append(peak)

    avg_time_us = (sum(times) / runs) * 1e6
    avg_peak = sum(peaks) / runs
    print(f"\t {label}: avg time = {avg_time_us:8.2f} us, avg peak memory = {avg_peak:7.0f} bytes")
    return avg_time_us, avg_peak


def main():

    # Graph (a) -- visited length when target 7 is found from source 0
    print("=== Graph a (undirected), source 0 -> target 7 ===")
    g_a_list = build_graph_undirected(GraphList)
    g_a_matrix = build_graph_undirected(GraphMatrix)
    print("Adjacency List:")
    bfs_list(g_a_list, 0, target=7)
    dfs_list(g_a_list, 0, target=7)
    print("Adjacency Matrix:")
    bfs_matrix(g_a_matrix, 0, target=7)
    dfs_matrix(g_a_matrix, 0, target=7)

    # Graph (b) -- visited length when target 'O' is found from source 'A'
    print("\n=== Graph b (directed), source A -> target O ===")
    g_b_list = build_graph_directed(GraphList)
    g_b_matrix = build_graph_directed(GraphMatrix)
    print("Adjacency List:")
    bfs_list(g_b_list, 'A', target='O')
    dfs_list(g_b_list, 'A', target='O')
    print("Adjacency Matrix:")
    bfs_matrix(g_b_matrix, 'A', target='O')
    dfs_matrix(g_b_matrix, 'A', target='O')

    # foot print statistics -- time and memory
    print("\n=== avg time + memory over 5 runs ===")

    # (graph_label, algorithm, implementation, callable)
    cases = [
        ("a", "BFS", "list",   lambda: bfs_list(g_a_list, 0, target=7, verbose=False)),
        ("a", "BFS", "matrix", lambda: bfs_matrix(g_a_matrix, 0, target=7, verbose=False)),
        ("a", "DFS", "list",   lambda: dfs_list(g_a_list, 0, target=7, verbose=False)),
        ("a", "DFS", "matrix", lambda: dfs_matrix(g_a_matrix, 0, target=7, verbose=False)),
        ("b", "BFS", "list",   lambda: bfs_list(g_b_list, 'A', target='O', verbose=False)),
        ("b", "BFS", "matrix", lambda: bfs_matrix(g_b_matrix, 'A', target='O', verbose=False)),
        ("b", "DFS", "list",   lambda: dfs_list(g_b_list, 'A', target='O', verbose=False)),
        ("b", "DFS", "matrix", lambda: dfs_matrix(g_b_matrix, 'A', target='O', verbose=False)),
    ]

    results = []
    last_graph = None
    for graph_label, algo, impl, fn in cases:
        if graph_label != last_graph:
            print(f"Graph-({graph_label}):")
            last_graph = graph_label
        label = f"{algo} {impl:6s}"
        avg_time_us, avg_peak = measure(label, fn)
        results.append({
            "graph": graph_label,
            "algorithm": algo,
            "implementation": impl,
            "avg_time_us": f"{avg_time_us:.4f}",
            "avg_peak_memory_bytes": f"{avg_peak:.0f}",
        })

    # write CSV
    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"\nresults written to {CSV_PATH}")


if __name__ == "__main__":
    main()

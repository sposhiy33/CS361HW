"""
CS361 - HW3
Problem 4 - plot 4-way heatmap (BFS/DFS x list/matrix) for time and memory
Author: Shrey Poshiya
"""

import csv
import os

import matplotlib.pyplot as plt
import numpy as np


RESULTS_DIR = "results"
CSV_PATH = os.path.join(RESULTS_DIR, "analysis_results.csv")
PLOT_PATH = os.path.join(RESULTS_DIR, "heatmap.png")

ALGOS = ["BFS", "DFS"]
IMPLS = ["list", "matrix"]


def load_results():
    rows = []
    with open(CSV_PATH, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def build_grid(rows, graph, metric):
    """
    build a 2x2 grid -- rows = BFS/DFS, cols = list/matrix
    """
    grid = np.zeros((len(ALGOS), len(IMPLS)))
    for i, algo in enumerate(ALGOS):
        for j, impl in enumerate(IMPLS):
            for r in rows:
                if r["graph"] == graph and r["algorithm"] == algo and r["implementation"] == impl:
                    grid[i, j] = float(r[metric])
                    break
    return grid


def draw_heatmap(ax, grid, title, unit, fmt="{:.2f}"):
    im = ax.imshow(grid, cmap="Blues", aspect="auto")
    ax.set_xticks(range(len(IMPLS)))
    ax.set_yticks(range(len(ALGOS)))
    ax.set_xticklabels(IMPLS)
    ax.set_yticklabels(ALGOS)
    ax.set_title(title)

    # annotate each cell with value -- pick text color based on cell brightness
    # Blues goes light -> dark, so dark text on low cells, white text on high cells
    vmin, vmax = grid.min(), grid.max()
    span = vmax - vmin if vmax > vmin else 1
    for i in range(len(ALGOS)):
        for j in range(len(IMPLS)):
            val = grid[i, j]
            color = "white" if (val - vmin) > 0.55 * span else "#0b2545"
            ax.text(j, i, fmt.format(val) + f"\n{unit}",
                    ha="center", va="center", color=color, fontsize=10)

    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)


def main():
    rows = load_results()

    fig, axes = plt.subplots(2, 2, figsize=(11, 9))

    # top row -- avg time
    draw_heatmap(axes[0, 0],
                 build_grid(rows, "a", "avg_time_us"),
                 "Graph-(a): avg time", "us")
    draw_heatmap(axes[0, 1],
                 build_grid(rows, "b", "avg_time_us"),
                 "Graph-(b): avg time", "us")

    # bottom row -- avg peak memory
    draw_heatmap(axes[1, 0],
                 build_grid(rows, "a", "avg_peak_memory_bytes"),
                 "Graph-(a): avg peak memory", "B",
                 fmt="{:.0f}")
    draw_heatmap(axes[1, 1],
                 build_grid(rows, "b", "avg_peak_memory_bytes"),
                 "Graph-(b): avg peak memory", "B",
                 fmt="{:.0f}")

    fig.suptitle("BFS vs DFS, Adjacency List vs Matrix (avg of 5 runs)", fontsize=13)
    plt.tight_layout()

    os.makedirs(RESULTS_DIR, exist_ok=True)
    plt.savefig(PLOT_PATH, dpi=150)
    print(f"saved heatmap to {PLOT_PATH}")


if __name__ == "__main__":
    main()

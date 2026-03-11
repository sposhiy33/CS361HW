""""
CS361 - HW2
Problem 2 - Hybrid Sort - Merge Sort with Insertion Sort
Author: Shrey Poshiya
"""

import math
import time
import random
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# set style for seaborn
sns.set_style("whitegrid")


## variables
N = [500, 2000, 8000]
K = [1,2,4,8,16,32,64]
numTrials = 5

# merge sort implementation
def mergeSort(arr, k):
    
    # change the lowest bound for return
    if len(arr) <= k:
        arr = insertionSort(arr)
        return arr

    mid = len(arr) // 2

    lower = mergeSort(arr[:mid], k)
    higher = mergeSort(arr[mid:], k)

    return merge(lower, higher)


def merge(A,B):

    # if i were not using python list, C would be iitialized to be length of len(A) + len(B)
    C = []
    a = 0
    b = 0

    # iterate over the two lists and merge
    while (a < len(A)) and (b < len(B)):
        if A[a] < B[b]:
            C.append(A[a])
            a += 1
        else:
            C.append(B[b])
            b += 1

    # if any elements missed from either, add them to the final list
    while (a < len(A)):
        C.append(A[a])
        a += 1
    
    while (b < len(B)):
        C.append(B[b])
        b += 1

    return C


def insertionSort(A):
   
    assert len(A) > 0, "error, ensure that provided list is NOT empty"

    for i in range(1, len(A)):
        
        # initialzie 
        key = A[i]
        j = i - 1
        
        # shift up any elements that are greater than the key
        while j >= 0 and key <= A[j]:
            A[j + 1] = A[j]
            j  -= 1

        # move the key behind the shited up elements
        A[j+1] = key

    return A


def main():

    # actual emperical results
    results = {}
    
    for n in N:
        sub_result = {}
        for k in K:
            sub_sub_result = []
            for _ in range(numTrials):
                # genreate random array
                # doing this to prevent duplicates in the list
                array = [i for i in range(n)]
                random_list = random.sample(array, len(array))

                start = time.time()
                sorted_array = mergeSort(random_list, k=k)
                end = time.time()

                total_time = end - start

                sub_sub_result.append(total_time)

            sub_result[f"{k}"] = sub_sub_result

        results[f"{n}"] = sub_result

    # plotting
    plot_data = []
    for n_str, k_times in results.items():
        n_val = int(n_str)
        for k_str, times in k_times.items():
            k_val = int(k_str)
            avg_sec = sum(times) / len(times)
            avg_ms = avg_sec * 1000
            plot_data.append({"k": k_val, "array_size": n_val, "avg_runtime_ms": avg_ms})

    df = pd.DataFrame(plot_data)

    plt.figure(figsize=(8, 5))
    sns.lineplot(data=df, x="k", y="avg_runtime_ms", hue="array_size", marker="o")
    for _, row in df.iterrows():
        plt.annotate(
            f"{row['avg_runtime_ms']:.3f}",
            (row["k"], row["avg_runtime_ms"]),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center",
            fontsize=8,
        )
    plt.xticks(K)
    plt.xlabel("Threshold value k")
    plt.ylabel("Average runtime (ms)")
    plt.title("Merge-insertion sort: threshold k vs average runtime (n=5)")
    plt.legend(title="Array size")
    plt.tight_layout()
    plt.show()

    print(results)


if __name__ == "__main__":
    main()

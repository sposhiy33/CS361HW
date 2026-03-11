"""
CS361 - HW2
Problem 3 - Counting Inversions
Author @Shrey Poshiya
"""

# merge sort implementation
def mergeSort(arr):
    """
    main merge sort function
    [arr] = list
    """
    if len(arr) <= 1:
        return (arr, 0)

    mid = len(arr) // 2

    lower_sorted, c1 = mergeSort(arr[:mid])
    higher_sorted, c2 = mergeSort(arr[mid:])
    merged, c3 = merge(lower_sorted, higher_sorted, 0)

    # overall the reccursive calls, continue adding up the inversions
    total_count = c1 + c2 + c3

    return merged, total_count


def merge(A,B,count):

    # if i were not using python list, C would be iitialized to be length of len(A) + len(B)
    C = []
    a = 0
    b = 0

    # iterate over the two lists and merge (this is done until one of the lists is completely merged)
    while (a < len(A)) and (b < len(B)):
        if A[a] < B[b]:
            C.append(A[a])
            a += 1
        else:
            C.append(B[b])
            b += 1
            # iterate inversion count -> number of elements that B[b] skips over in A
            count += len(A) - a

    # if any elements missed from either, add them to the final list
    # first A then B to ensure order
    while (a < len(A)):
        C.append(A[a])
        a += 1

    while (b < len(B)):
        C.append(B[b])
        b += 1

    return C, count


def main():

    arr1 = [1,2,3,4]
    arr2 = [4,3,2,1]
    arr3 = [2,4,1,3]

    # sort each of the arrays

    sorted_arr1, inversion_1 = mergeSort(arr1)
    sorted_arr2, inversion_2 = mergeSort(arr2)
    sorted_arr3, inversion_3 = mergeSort(arr3)

    print(f"{arr1} -> after merge sort: {sorted_arr1} -> number of inversions = {inversion_1}")
    print(f"{arr2} -> after merge sort: {sorted_arr2} -> number of inversions = {inversion_2}")
    print(f"{arr3} -> after merge sort: {sorted_arr3} -> number of inversions = {inversion_3}")


if __name__ == "__main__":
    main()


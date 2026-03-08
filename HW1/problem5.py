import math
import random


# create a random array of length 5
array = [random.randint(1, 100) for _ in range(5)]

# print the array
print(f"Initial array: {array}")

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        print(f"key is set as: {key}")
        while j >= 0 and key > A[j]:
            print(f"    Swapping {A[j]} and {key}")
            A[j + 1] = A[j]
            j -= 1
            print(f"        {A}")
        A[j + 1] = key
        print(f"    key is placed at index {j + 1}, array is now {A}")
    return A

print(f"Final sorted array: {insertion_sort(array)}")
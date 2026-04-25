"""
CS361 - HW3
Problem 1 - # of elements less than x
Author: Shrey Poshiya
"""

from minheap import RandomMinHeap


def lessThanX(minheap, x, k):
    """
    Use a traversal technique, we will use a queue to keep track of exploration.
    Initialize a count variable

    # the loop
    1. Traverse from the root node, first element of the minheap
    2. if root is less continue traversing to the children
       add the children of the root to the queue
        2a. increment the count by 1
    3. Dequeue element, and continue exploration from there
        3a. if one of the leaf nodes ends up being greater
            then dequeue then next child from the queue and continue
            the exploration from there


    - keep track of how many elements end up being less than k,
      return True when we hit the count == k
    - if we can do this before the queue empties out, return True
        - else if the queue empties before our count == k, return False
    """

    assert k > 0, "k must be greater than 0"

    heap = minheap.min_heap
    n = minheap.size

    assert k < n, "k must be less than the length of the minheap"

    count = 0
    # queue the root node (starting from here)
    queue = [0] 

    while len(queue) > 0:
        curr_idx = queue.pop(0)

        if heap[curr_idx] < x:
            count += 1
            if count >= k:
                return True

            # enqueue children if they exist
            left = (2 * curr_idx) + 1
            right = (2 * curr_idx) + 2
            if left < n:
                queue.append(left)
            if right < n:
                queue.append(right)

    return False


if __name__ == "__main__":

    # initialize the min heap
    minheap = RandomMinHeap(20)
    print(minheap.min_heap)

    # main code
    x = 30
    k = 5
    result = lessThanX(minheap, x, k)
    print(f"at least {k} elements less than {x}? {result}")

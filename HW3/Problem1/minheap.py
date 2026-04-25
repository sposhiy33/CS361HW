"""
min heap definition
@author: Shrey Poshiya
"""

import random
import math

class RandomMinHeap:

    def __init__(self, n):
        self.n = n
        assert n < 100, "more than 100 elements is not allowed"

        # initialize elements
        array = random.sample(range(1,100), n)
        print(array)
        
        # initialize minheap with math.inf
        self.min_heap = [math.inf for i in range(n)]
        self.size = 0
    
        # insert all the elements
        for item in array:
            self.insert(item)
            self.size += 1

    def insert(self, element):
        
        assert element not in self.min_heap, "element already in heap, no duplicates"

        # insert element at the end of min heap, first element that is still math.inf
        curr_idx = self.size
        self.min_heap[curr_idx] = element

        # check parent, if element is less, move it up
        parent_idx = int(math.floor((curr_idx - 1)/2))
        while parent_idx >= 0:
            curr_element = self.min_heap[curr_idx]
            parent_element = self.min_heap[parent_idx]
 
            if curr_element < parent_element:
                # swap
                self.min_heap[parent_idx] = curr_element
                self.min_heap[curr_idx] = parent_element

                # update the indicies
                curr_idx = parent_idx
                parent_idx = int(math.floor((curr_idx - 1)/2))

            else: break

        print(f"inserted element at index {curr_idx}")



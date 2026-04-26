"""
CS361 - HW3
Problem 3 -- Leetcode Rotting Oranges
Author: Shrey Poshiya
"""

from typing import List


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        # get starting positions of the twos
        twos = []
        ones = []
        for row, sublist in enumerate(grid):
            for col, element in enumerate(sublist):
                if element == 2:
                    twos.append((row, col))
                if element == 1:
                    ones.append((row, col))

        ## --- Address the trivial cases
        # if no starting rotten oranges, return null
        if (len(twos) == 0) and (len(ones) > 0):
            return -1 

        # if no starting oranges at all, return 0
        if (len(twos) == 0) and (len(ones) == 0):
            return 0


        ### --- Now for the real stuff
        # prelim variables
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        self.minute = 0
        self.rotten = [item for item in twos]
        # keep track of current and next level traversals for minute count
        # 2 queues as opposed to 1 in standard BFS
        self.level_current = [item for item in twos]
        self.level_next = []

        # do BFS propogation on the current level twos
        # increment minute by 1 on each propogation
        while len(self.level_current) > 0:

            # pop the whole level
            for _ in range(len(self.level_current)):
                item = self.level_current.pop(0)
                self.BFSPropogate(item)

            if len(self.level_next) == 0:
                break

            self.level_current = self.level_next
            self.level_next = []
            self.minute += 1

        # now that graph has been traversed, check if any oranges are still 1
        for row in grid:
            for element in row:
                if element == 1:
                    return -1

        return self.minute


    def BFSPropogate(self, source):

        fourmap = [(1,0), (0,1), (-1,0), (0,-1)]

        # in each direction, add vertex, if possible:
        for direction in fourmap:
            new_pos = tuple(a + b for a,b in zip(source, direction))

            if (0 <= new_pos[0] < self.m) and (0 <= new_pos[1] < self.n):
                if (new_pos not in self.rotten) and (self.grid[new_pos[0]][new_pos[1]] == 1):
                    self.level_next.append(new_pos)
                    self.rotten.append(new_pos)
                    self.grid[new_pos[0]][new_pos[1]] = 2


if __name__ == "__main__":

    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    print(f"grid: {grid1} --> expected 4 \n \t Result: {Solution().orangesRotting(grid1)}")

    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(f"grid: {grid2} --> expected -1 \n \t Result: {Solution().orangesRotting(grid2)}")

    grid3 = [[0,2]]
    print(f"grid: {grid3} --> expected 0 \n \t Result: {Solution().orangesRotting(grid3)}")

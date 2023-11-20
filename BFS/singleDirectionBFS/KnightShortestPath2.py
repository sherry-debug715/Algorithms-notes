"""
LintCode problem 630: https://www.lintcode.com/problem/630/
"""

from typing import (
    List,
)

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        # write your code here
        # create a counter variable to keep track of path, starting from 0
        # tranverse through the grid starting from grid[0][0]
        # add the (0, 0) to a queue 
        # while queue
        # pop out the first coordinates 
        # increment counter 
        # check 1. if the coordinates is (n - 1, m - 1), return counter. 
        #       2. if not, check it's inbounded valid neighbors, helper function 
        #       3. check if any of the neighbors are already in the  set
        #       4. add the valid neighbors to a queue 
        
        # edge case, return -1 if grid[0][0] == 1 or grid[n-1][m-1] == 1 

        end_row, end_col = len(grid) - 1, len(grid[0]) - 1 

        if grid[0][0] == 1 or grid[end_row][end_col] == 1:
            return -1 
        
        queue = collections.deque([(0, 0, 0)]) 

        while queue: 
            (r, c, level) = queue.popleft() 
            if (r, c) == (end_row, end_col):
                return level 
            neighbors = self.get_neighbors(r, c, grid) 

            for (n_row, n_col) in neighbors:
                queue.append((n_row, n_col, level + 1)) 
                grid[n_row][n_col] = 1
        
        return -1 
    
    def get_neighbors(self, row, col, grid):
        pos = [(row + 1, col + 2), (row - 1, col + 2), (row + 2, col + 1), (row - 2, col + 1)]      
        neighbors = [(row, col) for (row, col) in pos if self.inbound(row, col, grid)]

        return neighbors 

    def inbound(self, row, col, grid):
        row_bound = 0 <= row < len(grid)
        col_bound = 0 <= col < len(grid[0]) 
        if not row_bound or not col_bound:
            return False

        isBarrier = grid[row][col] == 1
        if isBarrier:
            return False

        return True












                    
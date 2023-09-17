"""
LintCode problem 115: https://www.lintcode.com/problem/115/
"""

from typing import (
    List,
)

class Solution:
    """
    @param obstacle_grid: A list of lists of integers
    @return: An integer
    """
    """
    Initialize a grid, path_tracker, populated with 0s.
    Fill the first row of path_tracker with 1, while checking if each pos in obstacle_grid is an obstacle, break if an 
    obstacle is found.
    Fill the first column of path_tracker with 1, while checking if each pos in obstacle_grid is an obstacle, break if an 
    obstacle is found.
    
    starting from second row and column 2 with r and c, check if obstacle_grid is 0, then add them up and 
    assign the result to path_tracker[r][c], else assign 0 to path_tracker[r][c]

    return path_tracker[n-1][m-1]
    """
    def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        row = len(obstacle_grid)
        col = len(obstacle_grid[0])
        path_tracker = [[0] * col for _ in range(row)] 

        for i in range(col): 
            if obstacle_grid[0][i]:
                break 
            path_tracker[0][i] = 1 
        
        for i in range(row):
            if obstacle_grid[i][0]:
                break 
            path_tracker[i][0] = 1 
        
        for r in range(1, row):
            for c in range(1, col):
                if obstacle_grid[r][c] == 0:
                    path_tracker[r][c] = path_tracker[r-1][c] + path_tracker[r][c-1] 
                else:
                    path_tracker[r][c] = 0

        return path_tracker[row - 1][col - 1] 

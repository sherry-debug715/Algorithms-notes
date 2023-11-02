"""
Lintcode problem 630: https://www.lintcode.com/problem/630/
"""
from typing import (
    List,
)

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    """
    Top to Bottom method:
    Check for edge case:
        1. if grid is empty
        2. if grid[0][0] is a barrie
    Initialize a number, row
    Initialize a number, col
    Initialize a list of tuples, pos, to document all positions that could lead to current pos.
    Initialize a grid, path_tracker, it should has the same row and col, with each pos filled with 
        float("inf"), since we are looking for minimal path
    populate path_tracker[0][0] with 0, as the starting point

# since the horse travel from left to right, the iteration should be from column to column, left to right 
    For range of col, with c:
        For range of row, with r:
            if grid[c][r] is 0:
                Iterate over pos with (row_from, col_from):
                    new_row = r + row_from
                    new_col = c + col_from
                    if both new_row and new_col are inbound:
                        path_tracker[r][c] = min(path_tracker[r][c], path_tracker[new_row][new_col] + 1) 
    
    check if path_tracker[row - 1][col - 1] is a barrie: 
        return -1
    else:
        return path_tracker[row - 1][col - 1]
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        if not grid or grid[0][0]:
            return -1

        row = len(grid) 
        col = len(grid[0]) 
        pos = [(-1, -2), (1, -2), (-2, -1), (2, -1)]
        path_tracker = [[float("inf")] * col for _ in range(row)] 

        path_tracker[0][0] = 0

        for c in range(col):
            for r in range(row):
                if grid[r][c] == 0:
                    for (row_from, col_from) in pos:
                        new_row = r + row_from
                        new_col = c + col_from 
                        if 0 <= new_row < row and 0 <= new_col < col:
                            path_tracker[r][c] = min(path_tracker[r][c], path_tracker[new_row][new_col] + 1) 
        
        if path_tracker[row - 1][col - 1] == float("inf"):
            return -1 
        
        return path_tracker[row - 1][col - 1]
    
    













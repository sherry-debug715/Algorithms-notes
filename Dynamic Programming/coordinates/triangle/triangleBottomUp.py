"""
Lintcode problem 109: https://www.lintcode.com/problem/109/?fromId=161&_from=collection
"""
from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    """
    Bottom up 
    Initialize a 2D list, min_path, filled with 0, with each inner list the length of inner list
    from triangle 
    Populate the last row of min_path with number from last row of triangle 
    Iterate from the last second row of min_path r
        Iterate over each column, c:
            min_path[r][c] = min(min_path[r + 1][c], min_path[r + 1][c+1]) + triangle[r][c]
    return min_path[0][0]
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        min_path = [[0] * (r + 1) for r in range(row)]

        for c in range(row):
            min_path[row - 1][c] = triangle[row - 1][c]  
        
        for r in range(row - 2, -1, -1):
            for c in range(r + 1):
                min_path[r][c] = min(min_path[r+1][c], min_path[r + 1][c + 1]) + triangle[r][c]
        
        return min_path[0][0]
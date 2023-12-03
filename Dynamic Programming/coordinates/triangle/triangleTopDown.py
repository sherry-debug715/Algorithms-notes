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
    Top to Bottom
    [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
    ]
    for every location of r,c, compare triangle[r-1][c-1] and triangle[r - 1][c+1]
    when c == 0 and c == end of the row, and r ==0, [r-1][c-1] or [r-1][c + 1] will go out of bound

    Initialize a 2D list, min_path, with each row the length of each row of triangle, populated with 0.
    Populate min_path[0][0] with trangle[0][0]
    Populate the first element from each row starting from row 1, with min_path[r][0] + triangle[r][0]
    Populate the last element from each row starting from row 1, with min_path[r][]

    For range of 2 and length of triangle, with r:
        for range of 1, r, with c:
            min_path[r][c] = min(min_path[r-1][c-1], min_path[r-1][c]) + triangle[r][c] 
    
    return min(min_path[length of triangle - 1])
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        row = len(triangle) 
        min_path = [[0] * (r + 1) for r in range(row)]
        min_path[0][0] = triangle[0][0]

        for r in range(1, row):
            min_path[r][0] = min_path[r - 1][0] + triangle[r][0] 
            min_path[r][r] = min_path[r - 1][r - 1] + triangle[r][r] 
        
        for r in range(2, row):
            for c in range(1, r):
                min_path[r][c] = min(min_path[r - 1][c - 1], min_path[r - 1][c]) + triangle[r][c]
        
        return min(min_path[row - 1])

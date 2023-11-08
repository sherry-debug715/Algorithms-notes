"""
Lintcode problem 28: https://www.lintcode.com/problem/search-a-2d-matrix
"""
from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
# [.  0  1  2. 3
#   1[1, 3, 5, 7],
#   2[10, 11, 16, 20],
                #   row * col - 1 -> 11
#   3[23, 30, 34, 50]
# ]

# L = 0
# R = len(matrix) * len(matrix[0]) - 1 
# M = (L + R) // 2 -> 2

# r = 2 // len(matrix) 
# c = 2 % len(matrix[0]) 
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) * len(matrix[0]) - 1 

        while L <= R:
            M = (L + R) // 2 
            row = M // len(matrix[0])
            col = M % len(matrix[0]) 

            if matrix[row][col] > target:
                R = M - 1
            elif matrix[row][col] < target:
                L = M + 1
            else:
                return True 
        
        return False  
            

"""
Lintcode problem 28: https://www.lintcode.com/problem/search-a-2d-matrix
"""
from typing import (
    List,
)
"""

Given that each row in the matrix is sorted in ascending order and the first element of each row is greater than the last element of the previous row, we can treat the 2D matrix as a flattened 1D list without actually restructuring it and apply binary search. 

The key to applying binary search in this context is to map a linear index to its corresponding 2D coordinates in the matrix. 
Here's a step-by-step breakdown of how this is achieved:

[
  [1,  3,  5,   7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

There are 12 total numbers stored, treat it as a 1D list, we have a begining index of 0 and end index of 11, we can easily get the middle point:
mid = (0 + 11) // 2 which is 5
now to convert 5 to the correct coordinates:
row = mid // total_columns (5 // 4 == 1)
col = mid % total_columns (5 % 4 == 1)
given us the correct indexes of mid, matrix[1][1]

# Complexity
- Time complexity:
O(log(m * n)), where m is the number of rows and n is the number of columns in the matrix. 

- Space complexity:
O(1)
"""

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

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
            

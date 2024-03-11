"""
Lintcode problem 38: https://www.lintcode.com/problem/38/
"""
from typing import (
    List,
)

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    """
    Initialize a starting row, r, len(matrix) - 1 
    Initialize a starting col, c, 0 
    Initialize a number, output, 0

    while both r and c are inbound:
        if matrix[r][c] > target:
            r -= 1
        elif matrix[r][c] < target:
            c += 1 
        else:
            output += 1 
            r -= 1
            c += 1 

    return output
    """
    # Time O(m + n): Because the algorithm moves one step (either right or up) in each iteration and because it can move at most m steps to the right (total number of columns) and n steps up (total number of rows) before it exits the matrix boundaries, the total number of steps (and thus the number of comparisons) is at most m+n. This results in a time complexity of O(m+n).
    # Space O(1)
    def search_matrix(self, matrix: List[List[int]], target: int) -> int:
        if not matrix:
            return 0 
        r = len(matrix) - 1 
        c = 0 
        output = 0 

        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                output += 1 
                r -= 1 
                c += 1

        return output

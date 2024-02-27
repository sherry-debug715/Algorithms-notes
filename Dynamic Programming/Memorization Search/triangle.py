"""
Lintcode problem 109: https://www.lintcode.com/problem/109/
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
    Initialize a function, _minimum_total, that takes in the following argument:
        1. triangle, 2. memo, set to {} 3. row, set to 0, 4, col, set to 0 
    function _minimum_total:
        base case: 
            1. if row == length of triangle, return 0 
            2. if (row, col) in memo: 
                return memo[(row, col)] 
        
        left = recursion(row + 1, col)
        right = recursion(row + 1, col + 1)
        memo[(row, col)] = min(left, right) + triangle[row][col]
        return memo[(row, col)]
    [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    The following algorithmn is based on a bottom up approach. It first compare the vallue of 
    adjacent numbers that the above number can move toward, choose the one with smaller value.
    When reaching the bottom of the stack, x == 0 and y == 0, memo[(x, y)] should be referencing
    the mininum path sum. 
    """
    # Time: O(n^2) 
    # Space: O(n^2), In the worst case, the result for each of the n * (n + 1) / 2 elements from the triangle tree will be stored in memo. Space complexity of the call stack is O(n) where n is the number of rows.
    def minimum_total(self, triangle: List[List[int]]) -> int:
        return self._minimum_total(triangle, {}, 0, 0) 
    
    def _minimum_total(self, triangle, memo, row, col):
        if row == len(triangle):
            return 0 
        if (row, col) in memo:
            return memo[(row, col)] 
        
        left = self._minimum_total(triangle, memo, row + 1, col)
        right = self._minimum_total(triangle, memo, row + 1, col + 1) 
        memo[(row, col)] = min(left, right) + triangle[row][col] 
        return memo[(row, col)]

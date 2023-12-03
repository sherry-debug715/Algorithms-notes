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
triangle = [
    [2],
    [3,4], 
    [6,5,7],
    [4,1,8,3]
] 
dp = [11,10,14,3]

    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        n = len(triangle)
        dp = triangle[-1]

        for i in range(n - 2, -1, -1): # i = 0
            for j in range(len(triangle[i])): # j = 0
                dp[j] = triangle[i][j] +  min(dp[j], dp[j + 1])
                
        return dp[0]
            



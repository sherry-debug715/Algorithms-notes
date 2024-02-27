from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    """
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0 
        
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]

        for idx in range(len(triangle[-1])):
            dp[-1][idx] = triangle[-1][idx] 
        
        for i in range(n - 2, -1 , -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        
        return dp[0][0]
        
    

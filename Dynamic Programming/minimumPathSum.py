# Lintcode problem 110: https://www.lintcode.com/problem/110/description?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    # Time: O(n * m)
    # Space: O(n * m)
    def min_path_sum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1 

        directions = [(-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])
        dp = [[float("inf")] * m for _ in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):
                for (r, c) in directions:
                    from_r, from_c = i + r, j + c
                    if from_r < 0 or from_r >= n or from_c < 0 or from_c >= m:
                        continue 
                    dp[i][j] = min(dp[i][j], dp[from_r][from_c] + grid[i][j]) 
        
        return dp[-1][-1]

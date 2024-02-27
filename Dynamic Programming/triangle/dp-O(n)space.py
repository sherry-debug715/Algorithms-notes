from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    # Time: O(n^2). The total number of iteration is the sum of 1+2+3+...+(n-1) = n(n - 1) / 2, which sum up to O(n^2)
    # Space: O(N) where n is the total number of rows of the input triangle. 
    def minimum_total(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0 
        
        n = len(triangle)
        path_sum = triangle[-1][::] 

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                path_sum[j] = min(path_sum[j], path_sum[j + 1]) + triangle[i][j] 
        
        return path_sum[0]

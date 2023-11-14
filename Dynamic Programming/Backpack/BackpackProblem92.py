"""
Lintcode problem 92: https://www.lintcode.com/problem/92/
"""

from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    """
    size = 10
              i-1
    A = [3,4,8,5]
    dp[i][j]=max(dp[i-1][j],dp[i-1][j-A[i-1]]+A[i-1]) 
    0[0,0,0,0,0,0,0,0,0,0,0]
    1[0,0,0,3,3,3,3,3,3,3,3]
    2[0,0,0,3,4,4,4,7,7,7,7]
    3[0,0,0,3,4,4,4,7,8,8,8] 
    4[0,0,0,3,4,5,5,7,8,9,9]
    """
    # Time: N((n + 1) * (size + 1))
    # Spaze: N((n + 1) * (size + 1))
    def back_pack(self, size: int, a: List[int]) -> int:
        if not a or size == 0:
            return 0 
        n = len(a)

        dp = [[0] * (size + 1) for _ in range(n + 1)] 

        for i in range(1, n + 1):
            for j in range(size + 1):
                if j >= a[i - 1]:
                    # zero one state, exclude the ith number or include it.
                    #  dp[i - 1][j - a[i - 1]] + a[i - 1] means the max size to form j - a[i - 1] the (i - 1)th elements from a list could form + a[i - 1] would evaluate to if choosing the ith number, the max size that could be formed to reach j.
                    # dp[i][j] then becomes the maximum of either including the i-th item or not including it, for a weight limit of j.
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + a[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j] 
        
        return dp[n][size]









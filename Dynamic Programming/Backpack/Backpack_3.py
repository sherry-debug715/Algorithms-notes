"""
lintcode problem 440: https://www.lintcode.com/problem/440/
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param v: an integer array
    @param m: An integer
    @return: an array
    """
    """
            i
    A = [2, 3, 5, 7]
    V = [1, 5, 2, 4]
    m = 10
    0[0,0,0,0,0,0,0,0,0,0,0]
    1[0,0,2,2,4,4,6,6,8,8,10]
    2[0,0,0,3,4,0,0,0,0,0,0]
    3[0,0,0,0,0,0,0,0,0,0,0]
    4[0,0,0,0,0,0,0,0,0,0,0]
    """
# Time: O(n * m)
# Space: O(n * m)
    def back_pack_i_i_i(self, a: List[int], v: List[int], m: int) -> int:
        if not a:
            return 0 
        
        n = len(a) 
        dp = [[0] * (m + 1) for _ in range(n + 1)] 

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= a[i - 1]:
                    # dp[i][j - a[i - 1]] + v[i - 1] effectively considers the scenario where the i-th item is included one more time (given it fits). The reason we don't need to explicitly count the item j // n times is that this is inherently managed by the iterative process of filling the DP array. Each time a size j is considered for the i-th item, the algorithm implicitly checks if adding one more instance of this item would increase the total value, without exceeding the capacity j.
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - a[i - 1]] + v[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j] 
        
        return dp[-1][-1]
# Optimized solution using an one-dimension list
    def back_pack_i_i_i(self, a: List[int], v: List[int], m: int) -> int:
        if not a:
            return 0 
        
        n = len(a) 

        dp = [0] * (m + 1)
        for i in range(n):
            for j in range(m + 1):
                if j >= a[i]:
                    dp[j] = max(dp[j], dp[j - a[i]] + v[i]) 

        return dp[-1]
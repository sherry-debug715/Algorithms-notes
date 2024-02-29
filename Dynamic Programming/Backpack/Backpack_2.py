"""
Lintcode problem 125: https://www.lintcode.com/problem/125/
"""
from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """
    # Time: O(n * m)
    # Space: O(n * m)
    def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
        if not a and not v:
            return 0 
        
        n = len(a) 
        dp = [[0] * (m + 1) for _ in range(n + 1)] 

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= a[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + v[i - 1]) 
                else:
                    dp[i][j] = dp[i - 1][j]             
        
        return dp[n][m]
# optimized solution
from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """
    # Time: O(n * m)
    # Space: O(n)
    # dp[j] 表示a数组中前i个物品里挑出一些放到dp数组中j的背包大小中的最大价值和
    def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
        if not a and not v:
            return 0 
        
        n = len(a) 
        dp = [0] * (m + 1) 

        for i in range(n):
            for j in range(m, a[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - a[i]] + v[i]) 

        return dp[m]


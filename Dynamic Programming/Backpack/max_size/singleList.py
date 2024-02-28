from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    """        3
    a = [3,4,8,5]
                 6
    [T,0,0,T,T,0,0,T,T,T,0]

    dp[j] = dp[j] or dp[j - A[i]]
    f[i][j]表示前i个物品选一些物品放入容量为j的背包中能否放满。
    """

    def backPack(self, m, A):
        if m == 0 or not A:
            return 0 
        
        dp = [0] * (m + 1)
        dp[0] = True 

        for i in range(len(A)):
            for j in range(m, -1, -1):
                if j < A[i]:
                    continue 
                dp[j] = dp[j] or dp[j - A[i]] 
        
        for n in range(m, -1, -1):
            if dp[n]:
                return n

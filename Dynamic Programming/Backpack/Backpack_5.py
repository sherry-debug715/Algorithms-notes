"""
Lintcode problem 563: https://www.lintcode.com/problem/563/
"""
from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    """
              i
     [1,2,3,3,7]

     [1,1,1,2,1,1,2,2]
    """
    # Time(O(n * target))
    # Space: O(target + 1)
    def back_pack_v(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0 
        
        n = len(nums) 
        # dp[j] represent the number of ways to fill a backpack of j with  i + 1 th elements from nums
        dp = [0] * (target + 1) 
        dp[0] = 1

        for i in range(n):
            for j in range(target, nums[i] - 1, -1): 
                dp[j] += dp[j - nums[i]]
        # print("dp", dp)
        return dp[-1]
                        

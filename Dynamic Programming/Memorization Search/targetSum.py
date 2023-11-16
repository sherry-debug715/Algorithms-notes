"""
lintcode problem 1208: https://www.lintcode.com/problem/1208/
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def find_target_sum_ways(self, nums: List[int], s: int) -> int:
        if not nums:
            return 0 
        
        return self.dfs(nums, 0, s, {}) 
    
    def dfs(self, nums, index, target_sum, memo):
        if (index, target_sum) in memo:
            return memo[(index, target_sum)]

        if index == len(nums):
            return 1 if target_sum == 0 else 0 
        
        plus = self.dfs(nums, index + 1, target_sum - nums[index], memo)
        minus = self.dfs(nums, index + 1, target_sum + nums[index], memo) 

        memo[(index, target_sum)] = plus + minus 

        return plus + minus 


from typing import (
    List,
)

class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums 
    """
    """
    在nums中找到能够组成接近sum(nums) // 2 的最大和 
    [T, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    def find_min(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        target = sum(nums) // 2
        row = len(nums) 

        dp = [0] * (target + 1) 
        dp[0] = True

        for i in range(row):
            for j in range(target, -1, -1):
                if j < nums[i]:
                    break 
                dp[j] = dp[j] or dp[j - nums[i]]
        
        for i in range(target, -1, -1):
            if dp[i]:
                diff = sum(nums) - i
                return abs(diff - i)
        


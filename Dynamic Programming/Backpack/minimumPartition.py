"""
Lintcode problem 724: https://www.lintcode.com/problem/724/
"""
from typing import (
    List,
)

class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums 
    """
# [
#     0[0, 0, 0, 0, 0, 0], 
#     1[0, 1, 1, 1, 1, 1], 
#     2[0, 1, 2, 3, 3, 3], 
#     3[0, 1, 2, 3, 4, 5], 
#     4[0, 1, 2, 3, 4, 5], 
# ]
# the below method will exceed the time limit, when the values of nums is too large, the dp size is also big.
    def find_min(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        target = sum(nums) // 2
        # state: dp[i][j] represents whether there exists a subsets from index 0 to i that it's max sum is <= j

        dp = [[0] * (target + 1) for _ in range(n + 1)] 

        # function
        for i in range(1, n + 1): 
            for j in range(0, target + 1): 
                if j >= nums[i - 1]: 
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j] 

        diff = sum(nums) - dp[n][target]
        return diff - dp[n][target]
    
# the optimized solution by using a single list 
# Time: O(n * target)
# Space: O(target)
class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums 
    """
    """
        n
    [1, 6, 11, 5] 
                                     j = 1
    dp = [0, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 7]
    """
    def find_min(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        target = sum(nums) // 2 
        # old approach: dp = [[0] * (target + 1) for _ in range(n + 1)] 
        # since for each row of i, the only data that matters is the value from dp[i - 1], therefore,
        # updating dp list through mutation could shrink the 2D list into single dimension. 
        dp = [0] * (target + 1) 
        for i in range(n):
            # stop at nums[i] - 1, because when j < nums[i], dp[j] is only going to inherit the previous value
            # from when i == i - 1.
            for j in range(target, nums[i] - 1, -1):
                    dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]) 

        diff = sum(nums) - dp[target]
        return diff - dp[target]
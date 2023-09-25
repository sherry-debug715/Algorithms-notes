"""
Lintcode problem 609: https://www.lintcode.com/problem/609/
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    """
    Edge case:
    1. If length of nums is 1 or nums array is empty:
        return 0 


    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums or len(nums) == 1:
            return 0

        nums.sort()
        counter = 0
        L, R = 0, len(nums) - 1

        while L < R:
            two_sum = nums[L] + nums[R] 
            if two_sum <= target:
                counter += (R - L)
                L += 1
            else:
                R -= 1
        return counter
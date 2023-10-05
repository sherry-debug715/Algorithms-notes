"""
Lintcode problem 443: https://www.lintcode.com/problem/443/?fromId=161&_from=collection
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    
    def two_sum2(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0 
        nums.sort()
        counter = 0 
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] > target:
                counter += (end - start)
                end -= 1
            else:
                start += 1 
        return counter 


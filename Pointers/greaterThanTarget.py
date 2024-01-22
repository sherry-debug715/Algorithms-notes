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
            # If the sum of the elements at nums[start] and nums[end] is greater than the target, 
            # it means that all elements from nums[start] to nums[end-1] (inclusive) paired with nums[end] 
            # will also be greater than target.
            if nums[start] + nums[end] > target:
                counter += (end - start)
                end -= 1
            else:
                start += 1 
        return counter 


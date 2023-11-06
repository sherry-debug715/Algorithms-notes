"""
lintcode 521: https://www.lintcode.com/problem/521/
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums.sort()

        j = 1  
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        
        return j
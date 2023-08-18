from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binary_search(self, nums: List[int], target: int) -> int:
        # write your code here
        return self._binary_search(0, len(nums) - 1, target, nums) 
    
    def _binary_search(self, start, end, target, nums):
        if start > end:
            return -1 
        
        mid = (start + end) // 2 
        if nums[mid] > target: 
            return self._binary_search(start, mid - 1, target, nums)
        if nums[mid] < target:
            return self._binary_search(mid + 1, end, target, nums)
        
        for n in range(start, mid):
            if nums[n] == target:
                return n 
        else:
            return mid 
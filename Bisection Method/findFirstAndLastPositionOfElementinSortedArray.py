"""
lintcode problem 1536: https://www.lintcode.com/problem/1536/
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    """
             s
    [5,7,7,8,8,10]
             m
               e
    """
    # Time: O(logN) * 2
    # Space: O(1)
    def search_range(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1] 
        
        start = self.find_start(nums, target)
        end = self.find_end(nums, target) 

        return [start, end]
    
    def find_start(self, nums, target):
        start, end = 0, len(nums) - 1 
        while start + 1 < end:
            mid = (start + end) // 2 
            if nums[mid] >= target:
                end = mid 
            else:
                start = mid 
        
        if nums[start] == target:
            return start 
        if nums[end] == target:
            return end 
        return -1 
    
    def find_end(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2 
            if nums[mid] <= target:
                start = mid 
            else:
                end = mid 
        
        if nums[end] == target:
            return end 
        if nums[start] == target:
            return start 
        return -1
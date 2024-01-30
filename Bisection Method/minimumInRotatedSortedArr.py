"""
Lintcode problem 159: https://www.lintcode.com/problem/159/?fromId=161&_from=collection
"""

from typing import (
    List,
)
# Time: O(logN)
# Space: O(1)
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        # write your code here
        left, right = 0, len(nums) - 1 

        while left + 1 < right: 
            mid = (left + right) // 2 
            if nums[mid] >= nums[right]: 
                left = mid 
            else:
                right = mid 
        
        return min(nums[left], nums[right])
"""
Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You can assume no duplicate exists in the array.

Problem 159 on Lintcode: https://www.lintcode.com/problem/159/
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    # Time: O(logN)
    # Space: O(1)
    def find_min(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 

        while left + 1 < right: 
            mid = (left + right) // 2 
            if nums[mid] >= nums[right]: 
                left = mid 
            else:
                right = mid 
        
        return min(nums[left], nums[right])
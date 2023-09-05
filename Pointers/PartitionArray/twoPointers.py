"""
Description
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

If all elements in nums are smaller than k, then return nums.length.
0<=nums.length<=2000
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        # edge cases:
        #  1. when nums is empty, return 0 
        #  2. If all elements in nums are smaller than k, then return nums.length

        # use two pointers, left and right 
        # while left <= right, so left and right break out, right < left
        # while nums[left] < k, incement left by one; while nums[right] >= k, 
        #   decrement right by one 
        #   else: swap left and right
        # break out of while loop, return left, because left will stop at the partition point.
        if not nums:
            return 0 

        if max(nums) < k:
            return len(nums) 

        left, right = 0, len(nums) - 1 
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1 
            while left <= right and nums[right] >= k:
                right -= 1 
            
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
          
        return left

#               l.          
#  [1, 2, 3, 4, 5, 5, 6, 7] k=5
#            r
    

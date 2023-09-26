"""
Lintcode problem 148: https://www.lintcode.com/problem/148/
"""
from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        # use number 1 as a pivot 
        # use two pointers left and right 
        # two pointers should traval towards each other.
        #   if num is 2, swap with right pointer, decrement right pointer, we don't increment index 
            # because we have no idea what number nums[right] was, therefore, we need index to reference it 
            # again and check on the next iteration.
        #   if num is 0, swap with left pointer, increment left pointer, also 
            # increment index, we can increment index because nums[index] was already visited. 
        #   only increment index if num is 1
        
        left, index, right = 0, 0, len(nums) - 1 

        while index <= right: 
            if nums[index] == 2:
                self.swap(index, right, nums)
                right -= 1 
            elif nums[index] == 0:
                self.swap(index, left, nums)
                left += 1 
                index += 1
            else:
                index += 1

        return nums
    
    def swap(self, idx1, idx2, nums):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1] 

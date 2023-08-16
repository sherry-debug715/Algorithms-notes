# Description
# Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

# Example1:
# Input: nums = [2, 7, 11, 15], target = 24. 
# Output: 5. 
# Explanation:
# 2 + 7 < 24
# 2 + 11 < 24
# 2 + 15 < 24
# 7 + 11 < 24
# 7 + 15 < 24

# Exmaple2:
# Input: nums = [1], target = 1. 
# Output: 0. 

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        # write your code here
        # edge case, if there is only one or 0 element in the list, return 0

        if not nums or len(nums) == 1:
            return 0
        
        # sort nums list to decrease time complexity
        nums.sort() 

        pointer1 = 0
        output = 0

        while pointer1 < len(nums) - 1:
            pointer2 = len(nums) - 1

            while pointer2 > pointer1:
                # since the input nums list has been sorted, once we found an outter most element matching the 
                # if condition, all the sums of numbers on the left side of this element with nums[pointer1] should be <= target
                if nums[pointer1] + nums[pointer2] <= target:
                    output += (pointer2 - pointer1)
                    break 
                pointer2 -= 1 

            pointer1 += 1
        
        return output
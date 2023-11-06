"""
lintcode problem 610: https://www.lintcode.com/problem/610/a
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    """
        Initialize a number, L1, 0
        Initialize a number, L2, 1
        While L2 < len(nums):
            diff = nums[L2] - nums[L1]
            if diff == abs(target):
                if L1 != L2:
                    return [nums[L1], nums[L2]] 
                else:
                    L2 += 1 
            elif diff < abs(target):
                L2 += 1
            else:
                L1 += 1

    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        L1, L2 = 0, 1 
        while L2 < len(nums):
            diff = nums[L2] - nums[L1]
            if diff == abs(target):
                if L1 != L2:
                    return [nums[L1], nums[L2]] 
                else:
                    L2 += 1 
            elif diff < abs(target):
                L2 += 1 
            else:
                L1 += 1 
            if L1 == L2:
                L2 += 1 
        return []



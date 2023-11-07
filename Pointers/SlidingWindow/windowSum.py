"""
Lintcode problem 604: https://www.lintcode.com/problem/604/
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    """
    Edge case:
    1. if array is empty, return []
    Initialize a number, window_sum = sum(nums[:k])
    Initialize a list, output, with window_sum.

    Iteratate over array from 1 to (length of nums - k + 1), with i:
        window_sum = window_sum - nums[i - 1] + nums[i + k - 1]
        add window_sum to output
    return output 
    """
    def win_sum(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return [] 

        window_sum = sum(nums[:k])
        output = [window_sum] 

        for i in range(1, len(nums) - k + 1):
            window_sum = window_sum - nums[i - 1] + nums[i + k - 1]
            output.append(window_sum) 
        
        return output 

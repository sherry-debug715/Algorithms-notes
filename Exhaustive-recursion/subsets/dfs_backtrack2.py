"""
lintcode problem 17: https://www.lintcode.com/problem/17/
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    """
    [
    [1,2,3] 
    [1,2]
    ]
    [1,2]

    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        result = []
        nums.sort()
        self._subsets(nums, 0, [], result) 
        return result 
    
    def _subsets(self, nums, startIndex, subset, result): 
        result.append([*subset])
        
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self._subsets(nums, i + 1, subset, result)
            subset.pop()


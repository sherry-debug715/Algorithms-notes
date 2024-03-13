# Lintcode problem 17: https://www.lintcode.com/problem/17/

from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        nums.sort()
        queue = [[]]

        i = 0

        while i < len(queue):
            subset = queue[i]
            for j in range(len(nums)):
                if len(subset) > 0 and subset[-1] >= nums[j]:
                    continue 
                new_sub = [*subset, nums[j]]
                queue.append(new_sub)
            i += 1
        
        return queue


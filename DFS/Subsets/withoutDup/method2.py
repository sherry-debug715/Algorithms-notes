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
        res = []
        if not nums:
            return [[]] 

        nums.sort()
        self.dfs(nums, 0, [], res)
        return res 
    
    def dfs(self, nums, startIndex, subsets, res):
        res.append([*subsets])

        for i in range(startIndex, len(nums)):
            subsets.append(nums[i])
            self.dfs(nums, i + 1, subsets, res) 
            # backtracking 
            subsets.pop()
        
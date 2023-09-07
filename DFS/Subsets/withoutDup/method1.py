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
        # write your code here
        res = [] 
        if not nums:
            return [[]] 
        
        nums.sort()
        self.dfs(0, nums, [], res) 
        return res 
    
    def dfs(self, index, nums, subsets, res):
        if index == len(nums):
            res.append([*subsets]) 
            return 
        # take index
        subsets.append(nums[index])
        self.dfs(index + 1, nums, subsets, res) 

        # not taken the element of the index 
        subsets.pop()
        self.dfs(index + 1, nums, subsets, res)


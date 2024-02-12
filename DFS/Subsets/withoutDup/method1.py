from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    # Time: O(2^n) - each element in the input list has two choices: either to be included in the current subset or not, leading to a total of O(2^n) possible subsets for a list of "n" elements.
    # Space: O(n) - the space complexity is to be considered from two main components: space used by the recursive call stack O(n) where n is the number of elements stored in input list, and the 2^n subsets stored in res.
    
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


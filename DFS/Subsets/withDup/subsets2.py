from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    # Time: O(N^2), worst case N is equal to the number of elements stored in the input lists, on average, when duplicates exists, the prunning reduces the size of N.
    # Space: O(N) + O(N*2^N) for the recursion stack + output space
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        res = [] 
        if not nums:
            return [[]] 
        
        nums.sort() 
        self.dfs(0, nums, [], res)
        return res 
    
    def dfs(self, startIndex, nums, subsets, res): 
        res.append([*subsets]) 

        for i in range(startIndex, len(nums)): 
            if i > startIndex and nums[i] == nums[i - 1]:
                continue
            subsets.append(nums[i]) 
            self.dfs(i + 1, nums, subsets, res) 

            subsets.pop()

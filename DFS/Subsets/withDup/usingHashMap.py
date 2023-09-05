from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        res = []
        hash_map = {}
        if not nums:
            return [[]]

        nums.sort() 
        self.dfs(nums, 0, [], res, hash_map)

        return res 
    
    def dfs(self, nums, start_index, subset, res, hash_map): 
        # print("cur sub", subset)
        if tuple(subset) in hash_map:
            return 
            # print("tuple(subset)", tuple(subset))
        res.append([*subset])
        hash_map[tuple(subset)] = True 
            # print("res", res)
        
        
        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, res, hash_map)
            subset.pop()

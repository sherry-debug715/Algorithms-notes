from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    # Time: O(N! * N) -> O(number of permutation * time spent to form each permutation)
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]] 
        
        visited = set() 
        res = []
        self.dfs(nums, visited, res, [])
        return res 
    
    def dfs(self, nums, visited, res, permutate): 
        if len(permutate) == len(nums):
            res.append(list(permutate)) 
            return 

        for num in nums:
            if num in visited:
                continue 
            
            permutate.append(num)
            visited.add(num)
            self.dfs(nums, visited, res, permutate)
            permutate.pop()
            visited.remove(num) 



from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
             we will sort your return value in output
    """
    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        if not a:
            return [] 
        a.sort()
        res = [] 
        self.dfs(a, k, target, res, 0, [])
        return res 
    
    def dfs(self, num_list, k, target_sum, res, start_index, subset): 
        if k == 0 and target_sum == 0:
            res.append([*subset]) 
            return
        
        if k < 0 and target_sum < 0:
            return 
        
        for i in range(start_index, len(num_list)): 
            subset.append(num_list[i]) 
            self.dfs(num_list, k - 1, target_sum - num_list[i], res, i + 1, subset) 
            subset.pop() 



"""
Given a set of candidate numbers candidates and a target number target. Find all unique combinations in candidates where the numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]
"""

from typing import (
    List,
)

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
             we will sort your return value in output
    """
    # Time: O(n**target/min), where n is the length of candidates, min is the number with minimal value from candidates list.
    # Space: O(n**target/min)
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. convert candidates list into a set then sort it to remove duplicate 
        # 2. Initialize a list, results, to keep track of all matching subs.
        # 3. initialize a helper function, dfs, that takes in sorted candidates, 
        #    curentIndex, curSubList, remainTarget, results as argument.
        #    1. if remainTarget < 0: return
        #    2. when remainTarget == 0, add curSubList to results, return. 
        #.   3. for i in range(currentIndex, len(candidates)):
        #       1. check if candidates[i] is > remainTarget, break. prunning
        #       2. add candidates[currentIndex] to curSubList
        #.      3. call dfs function, pass i + 1, remainTarget - candidates[currentIndex] to remainTarget
        #       4. remove the last element from curSubList, backtracking
        # 4. return results
        results = [] 

        if not candidates:
            return results

        new_candidates = sorted(list(set(candidates)))
        self.dfs(new_candidates, 0, [], target, results)
        return results 
    
    def dfs(self, candidates, start_index, cur_list, remain_target, results):
        if remain_target < 0:
            return 
        if remain_target == 0:
            results.append([*cur_list])
            return 
        
        for i in range(start_index, len(candidates)):
            if candidates[i] > remain_target:
                break 
            cur_list.append(candidates[i]) 
            self.dfs(candidates, i, cur_list, remain_target - candidates[i], results)
            cur_list.pop() 
        

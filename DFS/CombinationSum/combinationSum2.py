# Lintcode problem 153: https://www.lintcode.com/problem/153/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
             we will sort your return value in output
    """
    # Time: O(2^n)
    # Space: O(n * m)
    def combination_sum2(self, num: List[int], target: int) -> List[List[int]]:
        if not num:
            return []

        num.sort()
        res = []
        self.dfs(0, num, res, [], target)
        return res 
    
    def dfs(self, start_idx, num, res, sub, target):
        cur_sum = sum(sub)
        if cur_sum > target:
            return 
        if cur_sum == target:
            res.append([*sub])
            return 
        
        for i in range(start_idx, len(num)):
            if i > start_idx and num[i] == num[i - 1]:
                continue 
            sub.append(num[i])
            self.dfs(i + 1, num, res, sub, target)
            sub.pop()
  
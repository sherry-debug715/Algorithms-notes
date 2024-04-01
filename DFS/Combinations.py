# Lintcode problem 152: https://www.lintcode.com/problem/152/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
             we will sort your return value in output
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n:
            return []
        
        res = []
        self.dfs(1, n, k, res, [])
        return res 
    
    def dfs(self, cur_num, n, k, res, combination):
        if len(combination) == k:
            res.append([*combination])
            return 
        
        for num in range(cur_num, n + 1):
            combination.append(num)
            self.dfs(num + 1, n, k, res, combination)
            combination.pop()


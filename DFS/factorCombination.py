# Lintcode problem 1308: https://www.lintcode.com/problem/1308/description

from typing import (
    List,
)

class Solution:
    """
    @param n: a integer
    @return: return a 2D array
             we will sort your return value in output
    """
    def get_factors(self, n: int) -> List[List[int]]:
        if not n:
            return [] 
        
        res = []
        self.dfs(res, [n])
        return res 
    
    def dfs(self, res, sub):
        if len(sub) > 1:
            res.append([*sub])

        last_factor = sub.pop()  
        idx = 2 if len(sub) == 0 else sub[-1]  
        while idx <= last_factor // idx:
            if last_factor % idx == 0:
                sub.append(idx)
                sub.append(last_factor // idx)
                self.dfs(res, sub)
                sub.pop()
                sub.pop() 

            idx += 1 

        sub.append(last_factor)

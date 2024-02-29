# Lintcode problem 272: https://www.lintcode.com/problem/272/description?fromId=161&_from=collection

class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        if not n:
            return 1
        
        return self.dfs(n, 0, {}) 
    
    def dfs(self, n, cur_step, memo):
        if cur_step > n:
            return 0 

        if cur_step in memo:
            return memo[cur_step] 
        
        if cur_step == n:
            return 1 
        
        total_way = 0 
        for step in range(1, 4):
            total_way += self.dfs(n, cur_step + step, memo)
        
        memo[cur_step] = total_way 

        return total_way


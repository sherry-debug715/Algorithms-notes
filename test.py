# 93.44% time
# 64.69% space
class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 1 
        
        return self.dfs(n, 0, {}) 
    
    def dfs(self, n, cur_step, memo):
        if cur_step > n:
            return 0
        # memo[cur_step] reference the number of ways to climb to cur_step
        if cur_step in memo:
            return memo[cur_step]
        
        if cur_step == n:
            return 1 
        
        ways = 0
        for step in range(1, 3):
            ways += self.dfs(n, cur_step + step, memo) 
        
        memo[cur_step] = ways
        
        return ways
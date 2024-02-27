class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    """
m is row, n is col
    """
    def unique_paths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0 
        
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            dp[-1][i] = 1 
        
        for j in range(m):
            dp[j][-1] = 1 
        
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[r][c] = dp[r][c + 1] + dp[r + 1][c]
        
        return dp[0][0]

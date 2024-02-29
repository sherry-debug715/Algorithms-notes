class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    # [1, 1, 2, 4, 7]
    def climb_stairs2(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0] * (n + 1) 
        # if n == 1, there is only one way
        dp[0], dp[1] = 1, 1
        
        if n > 1:
            dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        return dp[n]

def backPack(m, A):
    n = len(A)
    # state: dp[i][j] represents whether there exists a subsets from index 0 to i that it's max sum is <= j

    dp = [[0] * (m + 1) for _ in range(n + 1)] 

    # function
    for i in range(1, n + 1):
        for j in range(0, m + 1): 
            if j >= A[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])
            else:
                dp[i][j] = dp[i - 1][j] 

    return dp[n][m] 
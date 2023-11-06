def backPack(m, A):
    n = len(A) 
    # state: dp[i][j] indicates whether there is a subset of numbers from 0 to i that can add up to j.
    # attention: it's a (n + 1) * (m + 1) matrix, instead of n * m.
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # initialize: from range 0 to 0, it's possible to sum up to 0.
    dp[0][0] = True 

    # function
    for i in range(1, n + 1):
        dp[i][0] = True 
        for j in range(1, m + 1):
            if j >= A[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j] 
    
    # answer
    for i in range(m, -1, -1):
        if dp[n][i]:
            return i 
        
    return -1

# m = 10  # The backpack's weight capacity
# A = [4, 3, 2, 5, 1]  # The weights of the items: Tent, Water Bottle, Food Supplies, Jacket, First Aid Kit
# i = 5  A[i - 1] == 1
# j = 1  dp[4][0]  
# [
#     0[True, False, False, False, False, False, False, False, False, False, False], 
#     1[True, False, False, False, True, False, False, False, False, False, False], 
#     2[True, False, False, True, True, False, False, False, False, False, False], 
#     3[True, False, True, True, True, True, True, False, False, False, False], 
#     4[True, False, True, True, True, True, True, True, True, True, True], 
#     5[True, True, True, True, True, True, True, True, True, True, True]
# ]
# output = 10







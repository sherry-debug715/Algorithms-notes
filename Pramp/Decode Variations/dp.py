# Pramp: https://www.pramp.com/challenge/r1Kw0vwG6OhK9AEGAy6L

def decodeVariations(S): # Time: O(n) Space: O(n)
  if S[0] == "0":
    return 0
  dp = [0] * (len(S) + 1) # Time: O(n) Space: O(n)
  dp[0], dp[1] = 1, 1
  
  for i in range(2, len(S) + 1): # Time: O(n - 2)
    if S[i - 1] != "0":
      dp[i] += dp[i - 1]
    two_digits = int(S[i-2:i])
    if 0 <= two_digits <= 26:
      dp[i] += dp[i-2]
      
  return dp[-1]
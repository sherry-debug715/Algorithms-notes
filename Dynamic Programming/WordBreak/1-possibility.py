"""
Lintcode problem 107: https://www.lintcode.com/problem/107/
"""

# DFS + memorization
# this is a brute force approach, which will exceed the max depth of recursion resulting to a runtime error. This problem is caused when an input string is very long, therefore, this problem is better solved by using tabulation method.
from typing import (
    Set,
)

class Solution:
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break(self, s: str, word_set: Set[str]) -> bool:
        if not s or not word_set:
            return False 
        # pruning: find the longest word from word_set, as there is no need to check if 
        #          a substring of s is in word_set if it's longer than the longest word from the set.
        max_length = len(max(word_set, key = len))

        return self.dp(s, word_set, 0, max_length, {}) 
    
    def dp(self, s, word_set, start, max_length, memo):
        if start in memo:
            return memo[start] 
        
        if start == len(s):
            return True  
        
        for end in range(start + 1, len(s) + 1):
            sub_str = s[start: end + 1]
            if len(sub_str) > max_length:
                break 
            if sub_str not in word_set:
                continue  

            if self.dp(s, word_set, end, max_length, memo):
                return True 

        memo[start] = False 

        return False 

from typing import (
    Set,
)

class Solution:
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    # Time: O(N^2)
    # Space: O(N)
    def word_break(self, s: str, word_set: Set[str]) -> bool:
        if not s:
            return True 
        
        if not word_set:
            return False

        n = len(s)
        # dp[i] indicate if substring s[:i + 1] is in dict 
        dp = [False] * (n + 1) 
        dp[0] = True 
        max_length = len(max(word_set, key = len))

        for i in range(1, n + 1):
            for j in range(1, max_length + 1): 
                if i < j:
                    break 
                # pruning: dp[i - j] represents whether the prefix of substring s[i - j: i] forms a word in wordDict. Skip if it doesn't.
                if not dp[i - j]:
                    continue 
                word = s[i-j:i]
                if word in word_set:
                    dp[i] = True 
                    break 
        
        return dp[n]


        


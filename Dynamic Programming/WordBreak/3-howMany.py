# Lintcode problem 683: https://www.lintcode.com/problem/683/?fromId=161&_from=collection

from typing import (
    Set,
)

class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    # Time: O(N^2)
    # Space: O(N)
    def word_break3(self, s: str, dict: Set[str]) -> int:
        if not dict:
            return 0
        
        n = len(s)
        max_length = len(max(dict, key=len))
        new_dict = {s.lower() for s in dict}
        dp = [0] * (n + 1) 
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, max_length + 1):
                if i < j:
                    break 
                if dp[i - j] == 0:
                    continue 
                word = s[i - j:i].lower()
                if word in new_dict:
                    dp[i] += dp[i - j] 
        
        return dp[-1]
    

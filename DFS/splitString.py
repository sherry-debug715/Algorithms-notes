# Lintcode problem 680: https://www.lintcode.com/problem/680/?fromId=161&_from=collection

from typing import (
    List,
)
# Time: O(2^n). The algorithm makes a recursive call for each possible split, leading to a growth factor of approximately 2^n in the worst case scenario where n is the length of the string.
class Solution:
    """
    @param s: a string to be split
    @return: all possible split string array
    """
    def split_string(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        
        res = []
        self.dfs(0, s, res, [])
        return res 
    
    def dfs(self, start_idx, s, res, sub):
        if start_idx == len(s):
            res.append([*sub])
            return 
        
        for i in range(start_idx, min(start_idx + 2, len(s))):
            sub.append(s[start_idx:i + 1])
            self.dfs(i + 1, s, res, sub)
            sub.pop() 

# Lintcode problem 624: https://www.lintcode.com/problem/624/?fromId=161&_from=collection

from typing import (
    Set,
)
from collections import deque

class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def min_length(self, s: str, dict: Set[str]) -> int:
        if not s or not dict:
            return 0
        
        queue = deque([s])
        visited = set([s])
        min_len = float("inf")

        while queue:
            cur_s = queue.popleft()
            for s in dict:
                pos = cur_s.find(s)
                while pos != -1:
                    if cur_s == s:
                        return 0

                    next_s = cur_s[:pos] + cur_s[pos + len(s):]
                    if next_s not in visited:
                        min_len = min(min_len, len(next_s))
                        queue.append(next_s)
                        visited.add(next_s)
                    pos = cur_s.find(s, pos + 1)
        
        return min_len

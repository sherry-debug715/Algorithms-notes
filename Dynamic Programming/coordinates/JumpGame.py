"""
LintCode problem 116: https://www.lintcode.com/problem/116/
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    """
    Logic: keep track of the previous number, i.e. where are you coming from 
    dp[i] 表示是否能跳到i, j代表上一步是从哪来的
    Edge case:
     1. if a list is empty, return False 
    
    Initialize a list, tracker, with length of a, populated with False. 
    Since it's made clear that the first element of a list >= 1, set 
    tracker[0] to True.

    For range of (1, length of a), with i:
        For range of i, with j:
            if tracker[j] and j + a[j] >= i:
                tracker[i] = True 
                break 
    
    return tracker[-1]
    """
    def can_jump(self, a: List[int]) -> bool:
        if not a:
            return False 
        
        tracker = [False] * len(a) 
        tracker[0] = True 

        for i in range(1, len(a)):
            for j in range(i):
                # 1. make sure where we are coming from is a valid point
                # 2. if the jump length of the j point could reach current i
                if tracker[j] and j + a[j] >= i:
                    tracker[i] = True
                    break 
        
        return tracker[-1]

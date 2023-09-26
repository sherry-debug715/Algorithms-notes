"""
Lintcode 144: https://www.lintcode.com/problem/144/?fromId=161&_from=collection
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        if not a:
            return [] 
        
        pos = [n for n in a if n > 0]
        neg = [n for n in a if n < 0] 

        if len(pos) > len(neg):
            a[::2], a[1::2] = pos, neg 
        else:
            a[::2], a[1::2] = neg, pos 

        return a
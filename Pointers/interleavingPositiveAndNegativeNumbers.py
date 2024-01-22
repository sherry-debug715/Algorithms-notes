"""
Lintcode 144: https://www.lintcode.com/problem/144/?fromId=161&_from=collection
"""
# Solution 1
from typing import (
    List,
)
# Time: O(n)
# Space: O(n)
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

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        
        if A is None or len(A) <= 1:
            return
        
        # Assume A does not contain 0
        
        lo, hi = 0, len(A)-1
        
        while lo <= hi:
            
            while lo <= hi and A[lo] < 0:
                lo += 1
                
            while lo <= hi and A[hi] > 0:
                hi -= 1
                
            if lo <= hi:
                A[lo], A[hi] = A[hi], A[lo]
                lo += 1
                hi -= 1
                
        # A[:lo] are neg number (amout: lo)
        # A[hi+1:] are pos number (amount: len(A)-hi-1)
        
        neg_count = lo
        pos_count = len(A)-hi-1
        
        # the amount of pos and neg number should at most diff by one
        if abs(neg_count - pos_count) > 1:
            return
        
        lo = 1 if neg_count >= pos_count else 0
        hi = len(A)-2 if pos_count >= neg_count else len(A)-1
        
        while lo < hi:

            A[lo], A[hi] = A[hi], A[lo]
            
            lo += 2
            hi -= 2
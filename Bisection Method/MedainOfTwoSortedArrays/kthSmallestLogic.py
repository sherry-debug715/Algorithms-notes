"""
lintcode problem 65: https://www.lintcode.com/problem/65/
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param b: An integer array
    @return: a double whose format is *.5 or *.0
    """
    """

    """
    def find_median_sorted_arrays(self, a: List[int], b: List[int]) -> float:
        n, m = len(a), len(b)
        # L is used to reference the number that's left to the number which R is referencing
        # R is used to reference the number that has just been eliminated from the option.
        L, R = 0, 0
        k = (n + m) // 2 
        even = (n + m) % 2 == 0
        P1, P2 = 0, 0

        for _ in range(k + 1):
            # move L pointer to point at the (_ - 1)ith smallest number before R pointer is moved.
            L = R
            # move P2 pointer
            if (P1 >= n or P2 < m and a[P1] > b[P2]):
                # use R pointer to reference the current _ith smallest number 
                R = b[P2]
                P2 += 1 
            # move P1 pointer
            else:
                R = a[P1]
                P1 += 1 
        
        if even:
            return (L + R) / 2
        else:
            return R
                





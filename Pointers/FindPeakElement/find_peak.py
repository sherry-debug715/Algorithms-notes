"""
Description
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.

Lintcode problem 75: https://www.lintcode.com/problem/75/
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        start, end = 0, len(a) - 1 

        while start + 1 < end:
            mid = (start + end) // 2 
            right = mid + 1 
            if a[mid] < a[right]:
                start = mid 
            elif a[mid] > a[right]:
                end = mid 
            else:
                if a[mid - 1] < a[mid] > a[right]:
                    return mid 
            
        if a[start] > a[end]:
            return start 
        else:
            return end 
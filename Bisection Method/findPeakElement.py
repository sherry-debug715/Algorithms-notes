"""
Lintcode problem 75: https://www.lintcode.com/problem/75/?fromId=161&_from=collection
"""
from typing import (
    List,
)
# Time: O(logN) for both average and worst cases
# Space: O(1)
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
                if a[left] < a[mid] > a[right]:
                    return mid 
            
        if a[start] > a[end]:
            return start 
        else:
            return end 

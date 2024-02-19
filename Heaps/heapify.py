# Lintcode problem 130: https://www.lintcode.com/problem/130/

from typing import (
    List,
)

class Solution:
    """
    @param a: Given an integer array
    @return: nothing
    """
    # Time: O(N)
    # Space: O(1)
    def heapify(self, a: List[int]):
        if not a:
            return [] 
        
        for idx in range(len(a) // 2, -1, -1):
            self.shift_down(idx, a)
        
        return a
    
    def shift_down(self, idx, a):
        while idx * 2 + 1 < len(a):
            smaller_son = idx * 2 + 1
            right_son = idx * 2 + 2
            if right_son < len(a) and a[right_son] < a[smaller_son]:
                smaller_son = right_son 
            if a[smaller_son] > a[idx]:
                break 
            a[smaller_son], a[idx] = a[idx], a[smaller_son]
            idx = smaller_son
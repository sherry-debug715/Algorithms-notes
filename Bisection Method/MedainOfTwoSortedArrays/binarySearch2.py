from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param b: An integer array
    @return: a double whose format is *.5 or *.0
    """
    # Time: O(log(min(n, m))) where n == len(a) and m == len(b)
    def find_median_sorted_arrays(self, a: List[int], b: List[int]) -> float:
        if not a and not b:
            return 0 
        
        shorter, longer = a, b
        if len(a) > len(b):
            shorter, longer = longer, shorter
        
        mid = (len(a) + len(b)) // 2
        
        return self._find_median_sorted_arrays(shorter, longer, mid)
    
    def _find_median_sorted_arrays(self, shorter, longer, half):
        L, R = 0, len(shorter) - 1 
        while True:
            m = (L + R) // 2
            left = half - m - 2

            longer_left = longer[left] if left >= 0 else float("-inf")
            shorter_left = shorter[m] if m >= 0 else float("-inf")
            longer_right = longer[left + 1] if left + 1 < len(longer) else float("inf")
            shorter_right = shorter[m + 1] if m + 1 < len(shorter) else float("inf")

            if longer_left <= shorter_right and shorter_left <= longer_right:
                # odd length
                if (len(shorter) + len(longer)) % 2 != 0:
                    return min(shorter_right, longer_right) 
                else:
                    mid_left = max(longer_left, shorter_left)
                    mid_right = min(shorter_right, longer_right)
                    return (mid_left + mid_right) / 2 

            elif shorter_left > longer_right:
                R = m - 1
            else:
                L = m + 1



                
# Lintcode problem 183: https://www.lintcode.com/problem/183/?fromId=161&_from=collection

from typing import (
    List,
)
# Time: O(N) + O(NlogN). Every step in the binary search involves an O(N)
#   operation from get_pieces function. 
# Space: O(1)
class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:
        if not l or k == 0:
            return 0

        left = 1
        right = min(max(l), sum(l) // k) 

        if left > right:
            return 0 
        
        while left + 1 < right:
            mid = (left + right) // 2 
            if self.get_pieces(l, mid) < k:
                right = mid 
            else:
                left = mid 
        
        if self.get_pieces(l, right) >= k:
            return right
        if self.get_pieces(l, left) >= k:
            return left
        return 0
        

    def get_pieces(self, nums, length):
        return sum( n // length for n in nums)

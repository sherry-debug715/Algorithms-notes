"""
Lintcode problem 685: https://www.lintcode.com/problem/685
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    # Time: O(n)
    # Space: O(n)
    def first_unique_number(self, nums: List[int], number: int) -> int:
        if not nums:
            return -1 
        
        visited = {}

        for n in nums:
            visited[n] = visited.get(n, 0) + 1
            if n == number:
                break 
        else:
            return -1 
        
        for n in visited:
            if visited[n] == 1:
                return n 

        return -1 

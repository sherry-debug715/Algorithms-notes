"""
Lintcode problem 62: https://www.lintcode.com/problem/62/?fromId=161&_from=collection
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: index of the target list 
    """
    """
        known: any left numbers is > any right numbers 
    """
    def search(self, a: List[int], target: int) -> int:
        # write your code here
        if not a:
            return -1 

        left, right = 0, len(a) - 1 
        # if list length > 1, enter the while loop
        while left + 1 < right:
            mid = (left + right) // 2 

            if a[mid] >= a[left]:
                if a[left] <= target <= a[mid]:
                    right = mid
                else:
                    left = mid 
            else:
                if a[mid] <= target <= a[right]:
                    left = mid 
                else:
                    right = mid
        # break out of the while loop, check the edge case where list length == 1 or 2
        if a[left] == target:
            return left 
        if a[right] == target:
            return right
        return -1 
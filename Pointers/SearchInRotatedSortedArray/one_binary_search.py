"""
Description
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
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
    # Time: O(logN)
    # Space: O(1)
    def search(self, a: List[int], target: int) -> int:
        if not a:
            return -1 

        left, right = 0, len(a) - 1 
        # if list length > 1, enter the while loop
        while left + 1 < right:
            mid = (left + right) // 2 
            # check if mid is in the left half or right half
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
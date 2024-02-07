"""
Lintcode problem 65: https://www.lintcode.com/problem/65/
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
    # Time(O(logmin(len(a), len(b))))
    # Space: O(1)
    def find_median_sorted_arrays(self, a: List[int], b: List[int]) -> float:
        # arrayA and arrayB are already sorted 
        # return number
        # need to consider if a list is empty 
        shorter_list, longer_list = a, b
        merged_length =  len(a) + len(b)
        merged_mid = merged_length // 2 

        if len(a) > len(b):
            shorter_list, longer_list = longer_list, shorter_list
        # The folowing code is not necessary, if a list is empty, the shorter_pointer and shorter_right will be set to float("-inf") and float("inf") respectively, therefore, enter the return statement.   
        # if not shorter_list:
        #     L, R = 0, len(longer_list) - 1
        #     mid = (L + R) // 2
        #     if len(longer_list) % 2 == 0:
        #         return ( longer_list[mid] + longer_list[mid + 1] ) / 2
        #     return longer_list[mid]
        
        left, right = 0, len(shorter_list) - 1 

        while True: 
            mid_shorter = (left + right) // 2 
            mid_longer = merged_mid - (mid_shorter + 1) - 1
            
            shorter_pointer = shorter_list[mid_shorter] if mid_shorter >= 0 else float("-inf") 
            shorter_right = shorter_list[mid_shorter + 1] if mid_shorter + 1 < len(shorter_list) else float("inf")
            longer_pointer = longer_list[mid_longer] if mid_longer >= 0 else float("-inf")
            longer_right = longer_list[mid_longer + 1] if mid_longer + 1 < len(longer_list) else float("inf")

            if (shorter_pointer <= longer_right and longer_pointer <= shorter_right):
                if merged_length % 2 == 0:
                    return (max(shorter_pointer, longer_pointer) + min(shorter_right, longer_right)) / 2
                return max(shorter_right, longer_right)
            elif shorter_pointer > longer_right:
                right = mid_shorter - 1
            else:
                left = mid_shorter + 1

    


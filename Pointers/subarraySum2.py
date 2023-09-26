"""
LintCode problem 404: https://www.lintcode.com/problem/404/?fromId=161&_from=collection
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    # Time: O(n)
    # Space: O(1)
    def subarray_sum_i_i(self, a: List[int], start: int, end: int) -> int:
        if not a:
            return 0 
        
        output = 0 
        left_sum, left_pointer = 0, 0
        right_sum, right_pointer = 0, 0
        for i in range(len(a)):
            num = a[i]
            left_pointer = max(left_pointer, i)
            right_pointer = max(right_pointer, i)
            if num > end:
                break
            while left_pointer < len(a) and a[left_pointer] + left_sum < start:
                left_sum += a[left_pointer]
                left_pointer += 1 
            while right_pointer < len(a) and a[right_pointer] + right_sum <= end:
                right_sum += a[right_pointer]
                right_pointer += 1 

            if right_pointer > left_pointer:
                output += right_pointer - left_pointer 
            # backtracking 
            if right_pointer > i:
                right_sum -= a[i] 
            if left_pointer > i:
                left_sum -= a[i]

        return output 


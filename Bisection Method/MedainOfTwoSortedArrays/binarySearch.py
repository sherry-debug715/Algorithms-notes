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
    """
    Initialize a variable, total_length, length A + length B
    Initialize a variable, mid, total_length // 2 
    Initialize two variables, shorter_list, longer_list, set them to a and b
    Initialize a left pointer, L, set it to 0 
    Initialize a right pointer, R, it should be the last index of the shorter_list

    while L <= R:
        Initialize a mid pointer, M, set it to (L + R) // 2 
        find the other pointer of the longer list, left, set it to mid - (M + 1) - 1
        initialize a variable, longer_to_right, set it to longer_list[left + 1] if it exist otherwise float("inf
        ")
        initialize a variable, shorter_to_right, set it to shorter_list[M + 1] if it exists or
        float("inf") 
        check if shorter[M] <= longer[L + 1] and if longer[L] <= shorter[M + 1]:
            break 
        check if shorter[M] > longer[L + 1]:
            R = M 
        check if longer[L] > shorter[M + 1]:
            L = M 
    
    if total_length % 2 == 0:
        take the larger value of shorter[M] to longer[L - 1], set it to larger if 
        take the smaller value of longer[L] to shorter[M + 1], set it to smaller
        return (larger + smaller) / 2 
    else:
        return min(longer[L + 1], shorter[M + 1])
    """
    def find_median_sorted_arrays(self, a: List[int], b: List[int]) -> float:
        shorter_list = a if len(a) <= len(b) else b
        longer_list = a if len(a) > len(b) else b 
        total_length = len(a) + len(b)
        mid = total_length // 2 

        L, R = 0, len(shorter_list) - 1

        if not shorter_list:
            if len(longer_list) % 2 == 0:
                return (longer_list[len(longer_list) // 2 - 1] + longer_list[len(longer_list) // 2]) / 2
            else:
                return longer_list[len(longer_list) // 2]

        while L <= R:
            M = (L + R) // 2
            longer_pointer = mid - (M + 1) - 1
            longer_to_right = longer_list[longer_pointer] if longer_list[longer_pointer] else float("inf")
            shorter_to_right = shorter_list[M + 1] if shorter_list[M + 1] else float("inf")
            if shorter_list[M] <= longer_list[longer_to_right] and longer_list[longer_pointer] <= shorter_list[shorter_to_right]:
                if total_length % 2 == 0:
                    left = max(longer_list[longer_pointer], shorter_list[M])
                    right = min(longer_list[longer_to_right], shorter_list[shorter_to_right])
                    return (left + right) / 2 
                else:
                    return min(longer_list[longer_pointer], shorter_list[M])
                
            if shorter_list[M] > longer_list[longer_to_right]:
                R = M - 1
            elif longer_list[longer_pointer] > shorter_list[shorter_to_right]:
                L = M + 1 
        

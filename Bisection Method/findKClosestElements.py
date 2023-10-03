"""
Lintcode problem 460: https://www.lintcode.com/problem/460/?fromId=161&_from=collection
"""

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array, sorted ascendingly 
    @param target: An integer
    @param k: An integer >= 0 
    @return: an integer array, sort by number - target, ascending or by number 
    if difference is the same, ascendingly.
    question: 1. is the difference calculated in absolute value?  
              2. will the input array A be empty 
    """
    """
    1. Use two pointers to look for position that the value of position: 
        A[left] < value <= A[right]
    2. Two pointers traverse towards outside, use merge sort style method to 
    compare their value while counting down k
    3. The final list returned contains numbers from the A list instead of the indexes.  
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        if not a:
            return []

        # locate the right pointer 
        right = self.locate_right(a, target)
        left = right - 1 

        output = [] 
        for _ in range(k): 
            if self.is_left_smaller(left, right, a, target):
                output.append(a[left])
                left -= 1 
            else:
                output.append(a[right])
                right += 1 
        
        return output 

    def locate_right(self, nums, target):
        start, end = 0, len(nums) - 1

        while start + 1 < end: 
            mid = (start + end) // 2 

            if nums[mid] >= target:
                end = mid 
            else:
                start = mid 

        if nums[end] >= target:
            return end 
        if nums[start] >= target:
            return start 
        
        # return the length as the farthest 'right' possible.
        # if the input list is [1, 2, 3, 4, 5] and target = 10
        return len(nums) 
    
    def is_left_smaller(self, left, right, nums, target): 
        if left < 0:
            return False 
        if right >= len(nums):
            return True
        
        return target - nums[left] <= nums[right] - target  
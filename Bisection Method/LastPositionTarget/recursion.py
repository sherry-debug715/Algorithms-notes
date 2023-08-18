from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def last_position(self, nums: List[int], target: int) -> int:
        # write your code here
        return self.binary_search(0, len(nums) - 1, target, nums)
    
    def binary_search(self, start, end, target, nums):
        if start > end:
            return -1 
        
        pivot = (start + end) // 2 
        if nums[pivot] < target:
            return self.binary_search(pivot + 1, end, target, nums)
        if nums[pivot] > target: 
            return self.binary_search(start, pivot - 1, target, nums)
        
        for n in range(end, pivot, -1):
            if nums[n] == target:
                return n 
        else:
            return pivot 
#    p  
# [1,2,2,4,5,5]. 2
# Lintcode problem 461: https://www.lintcode.com/problem/461/description?fromId=161&_from=collection
from typing import (
    List,
)
# Time: O(n)
# Space: O(1)
class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kth_smallest(self, k: int, nums: List[int]) -> int:
        if not nums or len(nums) < k:
            return 
        
        return self.quick_select(k - 1, nums, 0, len(nums) - 1)
    
    def quick_select(self, k, nums, start, end):
        left, right = start, end
        pivot = nums[(start + end) // 2] 

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left] 
                left += 1
                right -= 1
        
        if k >= left:
            return self.quick_select(k, nums, left, end)
        if k <= right:
            return self.quick_select(k, nums, start, right)

        return nums[k]

        
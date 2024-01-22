# Lintcode problem 5: https://www.lintcode.com/problem/5/description?fromId=161&_from=collection
from typing import (
    List,
)

# Time: O(n) average, O(n^2) worst
# Space: O(1)
class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        if not nums or k > len(nums):
            return 0 
        
        return self.quick_select(0, len(nums) - 1, k, nums)
    
    def quick_select(self, start, end, k, nums):   
        left, right = start, end 
        pivot = nums[(left + right) // 2] 

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1 
            while left <= right and nums[right] < pivot:
                right -= 1 
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left] 
                left += 1
                right -= 1 

        if start + k - 1 <= right:
            return self.quick_select(start, right, k, nums)
        if start + k - 1 >= left:
            return self.quick_select(left, end, k - (left - start), nums) 
        
        return nums[right + 1]
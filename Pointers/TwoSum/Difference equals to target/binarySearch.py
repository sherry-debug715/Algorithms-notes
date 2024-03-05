# Lintcode problem 610: https://www.lintcode.com/problem/610/

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    # Time: O(NlogN)
    # Space: O(1)
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return 
        
        for i in range(len(nums)):
            search_num = abs(target) + nums[i]
            if self.binary_search(search_num, i + 1, nums):
                return [nums[i], search_num] 
    
    def binary_search(self, target, left, nums):
        l, r = left, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                return True 
        
        if nums[l] == target or nums[r] == target:
            return True
        return False
